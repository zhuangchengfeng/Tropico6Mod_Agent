# Tropico 6 Modding 工具链

请直接接入你的 Agent，将本文件给他即可。使用前修改下方游戏目录路径。

## 前置准备

游戏根目录: `C:\TP6\Tropico 6`
游戏 Paks 目录: `C:\TP6\Tropico 6\Tropico6\Content\Paks`

## 目录结构

```
E:\Tropico6Modding\
├── README.md
├── CLAUDE.md                     ← Agent 必读（详细工作流）
├── modtool.py                    ← 模组管理 CLI（主力工具）
├── _game_extract/                ← 游戏源文件（只读，永不修改）
│   └── Tropico6/Content/Blueprints/Buildings/
├── MyMod/
│   ├── json/                     ← 可编辑的 JSON 文件
│   ├── files/                    ← .uasset + .uexp（由 fromjson 生成）
│   └── pak/z_MyMod.pak
├── _my_mods/                     ← 自定义独立 mod（手动修改 uasset）
│   ├── Highschool/
│   ├── NuclearPowerPlant/
│   └── _path/                    ← 每个 mod 的打包路径配置
├── finish_paks/                  ← 打包输出目录（所有 pak 汇总）
├── _path.txt                     ← MyMod 打包路径配置
├── UAssetGUI.exe                 ← uasset ↔ json 互转
├── UnrealPakTool/
│   ├── UnrealPak.exe             ← 提取游戏 pak（UE 4.25.3）
│   └── UnrealPak[v5_UE4.20].exe  ← 打包 mod pak（UE 4.20）
└── 建筑中英对照表.txt            ← 中文建筑名 → 英文目录名
```

## 工具

| 工具 | 用途 |
|------|------|
| `modtool.py` | **模组管理 CLI**（日常主力） |
| `UAssetGUI.exe` | uasset ↔ json 互转（modtool 自动调用） |
| `UnrealPakTool/UnrealPak.exe` | 从游戏提取 pak（4.25.3） |
| `UnrealPakTool/UnrealPak[v5_UE4.20].exe` | 打包 mod pak（4.20，modtool 自动调用） |

## modtool.py 使用

日常操作一律用 `modtool.py`，无需手动调用 UAssetGUI / UnrealPak。

| 命令 | 用途 |
|------|------|
| `python modtool.py find <关键词>` | 搜索建筑中文名 → 英文目录 |
| `python modtool.py convert <建筑名>` | 一键查表 + cp + tojson（仅首次） |
| `python modtool.py info [json名]` | 查看属性值，无参数则列出所有 JSON |
| `python modtool.py set <json> <属性> [值]` | 读取/修改属性 |
| `python modtool.py stock` | 批量改所有生产建筑库存 / 生产率 |
| `python modtool.py housing` | 批量翻倍住宅容量 |
| `python modtool.py package` | 打包所有 mod 到 `finish_paks/`（自动 compress） |
| `python modtool.py deploy` | 复制 `finish_paks/` 下所有 pak 到游戏目录 |
| `python modtool.py full` | fromjson-all + package + deploy 一键完成 |
| `python modtool.py status` | 查看当前修改状态 |

### 典型会话

```bash
# 改警卫塔伤害到 1000
python modtool.py find 警卫塔
python modtool.py convert ColonialGuardTower   # 仅首次
python modtool.py set BP_ColonialGuardTower RangeMin 1000
python modtool.py set BP_ColonialGuardTower RangeMax 1000
python modtool.py full                         # 打包部署

# 批量改库存
python modtool.py stock --capacity=50000 --rate=20
python modtool.py full
```

## 工作流

```
首次修改某建筑 → convert（cp + tojson）→ 得到 JSON
之后改同一建筑 → set（直接改已有 JSON）
打包部署       → full（fromjson-all → hexpatch → package → deploy）
```

所有 pak 输出到 `finish_paks/`，自动加 `-compress` 压缩，每个 pak 独立。

## 自定义独立 Mod

手动直接修改 uasset 的 mod 放 `_my_mods/` 下：

```
_my_mods/
├── Highschool/                   # 修改后的 uasset + uexp
├── NuclearPowerPlant/
└── _path/
    ├── _path_Highschool.txt      # 格式: "源文件夹\*" "挂载点/"
    └── _path_NuclearPowerPlant.txt
```

`package` 会自动扫描 `_my_mods/` 下所有有对应 `_path` 配置的文件夹，与 MyMod 一起打包。

## 注意事项

1. **永远不要修改 `_game_extract/`**，那是只读的原始数据
2. **一个建筑只 tojson 一次**，之后直接编辑已有 JSON
3. 必须用本机游戏提取的 V21 文件，网上旧版会导致闪退
4. 提取游戏 pak 加 `-Filter="*关键词*"` 秒出结果
5. FloatProperty/ByteProperty 修改需要执行 `hexpatch`（`full` 命令自动执行）
