# Tropico 6 Modding — Agent 必读

## 绝对路径铁律

**以下两个地方都必须用绝对路径，一个相对就炸：**

1. `_path.txt` 内容：`"E:\Tropico6Modding\MyMod\files\*" "../../../Tropico6/Content/"`
2. 打包命令的 `-Create=` 参数：`-Create="E:\Tropico6Modding\_path.txt"`

完整打包命令（别拆开）：
```bash
echo '"E:\Tropico6Modding\MyMod\files\*" "../../../Tropico6/Content/"' > _path.txt
./UnrealPakTool/UnrealPak[v5_UE4.20].exe "E:\Tropico6Modding\MyMod\pak\z_MyMod.pak" -Create="E:\Tropico6Modding\_path.txt"
```

`-Create=_path.txt` 相对路径 → `Failed to load` → 别反复试了，换绝对路径就行。

## 工具

| 工具 | 用途 | 引擎版本 |
|------|------|----------|
| `UnrealPakTool/UnrealPak.exe` | 从游戏 **提取** pak | 4.25.3 |
| `UnrealPakTool/UnrealPak[v5_UE4.20].exe` | **打包** mod pak | 4.20 |
| `UAssetGUI.exe` | uasset ↔ json | — |
| `UnrealLocres.exe` | locres → csv | — |
| `modtool.py` | **模组管理 CLI**（主力） | — |

提取用 4.25.3，打包用 4.20。反过来提取会报 magic number 错，打包会报 DDC 错。

## modtool.py 使用

**日常操作一律用 `modtool.py`，不要再单独调 UAssetGUI / UnrealPak。**

| 命令 | 用途 |
|------|------|
| `python modtool.py find <关键词>` | 搜索建筑中文名→英文目录 |
| `python modtool.py convert <建筑名>` | 一键查表+cp+tojson（仅首次用） |
| `python modtool.py info [json名]` | 查看属性值，无参数则列出所有 JSON |
| `python modtool.py set <json> <属性> [值]` | 读取/修改属性 |
| `python modtool.py stock` | 批量改所有生产建筑库存30000/生产10x |
| `python modtool.py housing` | 批量翻倍住宅容量 |
| `python modtool.py fromjson-all` | 所有 JSON → uasset+uexp |
| `python modtool.py hexpatch` | 修复 fromjson 遗漏的 FloatProperty/ByteProperty |
| `python modtool.py package` | 打包所有 mod 到 finish_paks/（自动 fromjson-all + hexpatch + compress） |
| `python modtool.py deploy` | 复制 finish_paks/ 下所有 pak 到游戏目录 |
| `python modtool.py full` | fromjson-all + package + deploy 一键 |
| `python modtool.py status` | 查看当前修改状态 |

**典型会话示例：**

```bash
# 用户说：改警卫塔伤害到1000
python modtool.py find 警卫塔                    # → ColonialGuardTower
python modtool.py convert ColonialGuardTower     # 仅首次
python modtool.py set BP_ColonialGuardTower RangeMin 1000
python modtool.py set BP_ColonialGuardTower RangeMax 1000
python modtool.py full                           # 打包部署

# 用户说：把库存全改到50000，生产率20x
python modtool.py stock --capacity=50000 --rate=20
python modtool.py full
```

## 工作流

```
_game_extract/源文件 → (首次)tojson → MyMod/json/ → 编辑已有json → fromjson → MyMod/files/ → 打包 → finish_paks/ → deploy → 游戏Paks/
```

**重要规则：一个建筑只 tojson 一次。** 首次修改某建筑时从 `_game_extract` 转 json，之后改同一建筑的其他属性，直接编辑已有的 json 文件，**不要重新 tojson**，否则会覆盖之前的改动。

每一步：

1. **查对照表**：`python modtool.py find <中文名>`
2. **convert**（仅首次）：`python modtool.py convert <建筑名>` 一键 cp+tojson
3. **编辑已有 JSON**：`python modtool.py set <json> <属性> <值>`
4. **打包部署**：`python modtool.py full` 一键 fromjson+打包+部署

### 自定义独立 mod

自己手动改 uasset 的独立 mod 放 `_my_mods/` 下，每个 mod 一个文件夹：

```
_my_mods/
├── Highschool/             # 文件夹名 = mod 名
│   ├── BP_Highschool.uasset
│   └── ...
├── NuclearPowerPlant/
│   └── ...
└── _path/
    ├── _path_Highschool.txt       # 格式: "源文件夹\*" "挂载点/"
    └── _path_NuclearPowerPlant.txt
```

`package` 和 `full` 会自动扫描 `_my_mods/` 下所有有对应 `_path` 配置的文件夹，与 MyMod 一起打包到 `finish_paks/`。

新增自定义 mod：
1. 在 `_my_mods/` 下新建文件夹，放入 uasset+uexp
2. 在 `_my_mods/_path/` 下新建 `_path_<文件夹名>.txt`，指向该文件夹和游戏内挂载路径

**例外场景**（modtool 不覆盖的）：
- 直接编辑 JSON 修改复杂嵌套结构时的手动操作
- 提取游戏 pak 用 `UnrealPakTool/UnrealPak.exe`

## 避坑

- 必须用本机游戏提取的 V21 文件，网上旧版文件会导致鼠标悬停就闪退（EXCEPTION_ACCESS_VIOLATION）
- 提取游戏 pak 加 `-Filter="*关键词*"` 能秒出结果，别全量解包单文件
- 属性里 `DamagePerWorker` 是 `T6Range` 结构体，值在嵌套的 `RangeMin`/`RangeMax` 里，别改外层
- `JobCapacity` 类型是 `Byte`，值超过 255 会截断
- **fromjson bug**: FloatProperty/ByteProperty 写入 uexp 不生效。`modtool.py full` / `package` 会自动执行 hexpatch 修正。如需手动：`python modtool.py hexpatch`
- **AgentMovementData** 等不在 `Blueprints/Buildings/` 下的文件，`fromjson-all` 不会处理。`hexpatch` 命令会自动从源拷贝 + 打补丁
