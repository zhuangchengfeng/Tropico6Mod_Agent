# Tropico 6 Modding 工具链

## 前置准备

**请先填入你的游戏安装路径：**

```
游戏根目录: C:\TP6\Tropico 6
游戏Paks目录: C:\TP6\Tropico 6\Tropico6\Content\Paks
```

## 工具说明

| 工具 | 路径 | 用途 |
|------|------|------|
| `UnrealPak.exe` | `UnrealPakTool/UnrealPak.exe` | **从游戏提取** pak 文件（UE 4.25.3 版本，兼容游戏的自定义 pak 格式） |
| `UnrealPak[v5_UE4.20].exe` | `UnrealPakTool/UnrealPak[v5_UE4.20].exe` | **打包** mod pak（UE 4.20 版本，与游戏引擎版本匹配） |
| `UAssetGUI.exe` | `UAssetGUI.exe` | `.uasset/.uexp` ↔ `.json` 互转 |
| `UnrealLocres.exe` | `UnrealLocres.exe` | `.locres` → `.csv` 导出游戏本地化文本 |

## 第一次使用：初始化

### 步骤 1：解包游戏主文件

将 `<游戏Paks目录>/pakchunk0-WindowsNoEditor.pak` 全部解包到 `_game_extract/`：

```bash
UnrealPakTool/UnrealPak.exe "<游戏Paks目录>/pakchunk0-WindowsNoEditor.pak" -Extract "_game_extract"
```

约 19GB，只需执行一次。之后所有源文件从 `_game_extract/Tropico6/Content/` 获取。

### 步骤 2：导出中文对照表

```bash
UnrealLocres.exe export "_game_extract/Tropico6/Content/Localization/Game/zh-Hans/Game.locres" -f csv -o "_zh_locres.csv"
```

### 步骤 3：生成建筑中英对照表

运行以下 Python 脚本，生成 `建筑中英对照表.txt`：

```python
import csv, os

zh = {}
with open('_zh_locres.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 2 and row[1].strip():
            zh[row[0]] = row[1]

mapping = {}
with open('_game_extract/Tropico6/Content/Localization/CSV/LocaSourceTable.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        if len(row) >= 2:
            eng = row[1].strip()
            cn = zh.get('/' + row[0].strip(), '')
            if cn and 2 <= len(eng) <= 40:
                mapping[eng] = cn

dirs = []
for root, subdirs, files in os.walk('_game_extract/Tropico6/Content/Blueprints/Buildings'):
    for d in subdirs:
        dirs.append(d)

with open('建筑中英对照表.txt', 'w', encoding='utf-8') as out:
    for d in sorted(set(dirs)):
        cn = mapping.get(d, '')
        if cn:
            out.write(f'{cn}|{d}\n')
```

完成后删除临时的 `_zh_locres.csv`。

## 目录结构

```
E:\Tropico6Modding\
├── README.md                     ← 本文件
├── _game_extract/                ← 游戏源文件（只读，永不修改）
│   └── Tropico6/Content/
│       ├── Blueprints/Buildings/ ← 所有建筑蓝图
│       ├── Localization/         ← 本地化文本
│       └── ...
├── MyMod/
│   ├── json/                     ← 可编辑的 JSON 文件（改这里）
│   ├── files/                    ← 修改后转换的 .uasset + .uexp
│   │   └── Blueprints/Buildings/ ← 与游戏内路径对应
│   └── pak/                      ← 打包输出
├── _path.txt                     ← 打包路径配置
├── UAssetGUI.exe
├── UnrealLocres.exe
├── UnrealPakTool/
│   ├── UnrealPak.exe             ← 提取用
│   └── UnrealPak[v5_UE4.20].exe  ← 打包用
└── 建筑中英对照表.txt            ← 中文建筑名 → 英文目录名
```

## 日常修改流程

用户只需说出**中文建筑名 + 要改的属性 + 目标值**，Agent 按以下步骤全自动执行：

### 步骤 1：查表定位

从 `建筑中英对照表.txt` 查找中文名对应的英文目录名。

例如：「警卫塔」→ `ColonialGuardTower` → 目录 `Colonial/ColonialGuardTower/`

### 步骤 2：拷贝源文件

```bash
cp "_game_extract/Tropico6/Content/Blueprints/Buildings/<目录>/<主蓝图>.uasset" "MyMod/files/Blueprints/Buildings/<目录>/"
cp "_game_extract/Tropico6/Content/Blueprints/Buildings/<目录>/<主蓝图>.uexp" "MyMod/files/Blueprints/Buildings/<目录>/"
```

### 步骤 3：转为 JSON

```bash
UAssetGUI.exe tojson "_game_extract/Tropico6/Content/Blueprints/Buildings/<目录>/<主蓝图>.uasset" "MyMod/json/<主蓝图>.json" 26
```

引擎版本参数 `26` = UE 4.26（游戏实际运行的引擎版本）。

### 步骤 4：修改 JSON

直接编辑 `MyMod/json/<主蓝图>.json` 中的 `Value` 字段。

常见属性对照：
- `StructurePoints` — 建筑血量
- `JobCapacity` — 岗位数
- `DamagePerWorker` → `RangeMin` / `RangeMax` — 伤害范围
- `ShotsBeforeReload` — 换弹前射击次数
- `AggroRange` — 警戒范围
- `MonthlyWageBase` → `Value` — 月薪
- `UpkeepBase` → `Value` — 维护费
- `WorkDuration` — 工作时长
- `JobQualityBase` — 岗位质量

### 步骤 5：转回 uasset

```bash
UAssetGUI.exe fromjson "MyMod/json/<主蓝图>.json" "MyMod/files/Blueprints/Buildings/<目录>/<主蓝图>.uasset"
```

这会同时生成/更新 `.uasset` 和 `.uexp`。

### 步骤 6：打包

```bash
UnrealPakTool/UnrealPak[v5_UE4.20].exe "MyMod/pak/z_MyMod.pak" -Create="_path.txt"
```

`_path.txt` 内容固定为：
```
"<项目绝对路径>\MyMod\files\*" "../../../Tropico6/Content/"
```

### 步骤 7：部署

```bash
cp "MyMod/pak/z_MyMod.pak" "<游戏Paks目录>/z_MyMod.pak"
```

同时清理旧版 pak（如 `z_Watchtower.pak`），避免冲突。

## 注意事项

1. **永远不要修改 `_game_extract/` 中的文件**，那是只读的原始数据
2. **提取用 `UnrealPak.exe`（4.25.3），打包用 `UnrealPak[v5_UE4.20].exe`（4.20）**，反过来会报错
3. 修改的文件必须来自**本机游戏版本**，不能用网上下载的旧版文件，否则游戏会闪退
4. `z_` 前缀的 pak 加载优先级最高（字母序最后）
5. 如果新增修改的建筑，文件会自动归入同一个 `z_MyMod.pak`，无需单独打包
