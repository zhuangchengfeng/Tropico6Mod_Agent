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

提取用 4.25.3，打包用 4.20。反过来提取会报 magic number 错，打包会报 DDC 错。

## 工作流

```
_game_extract/源文件 → tojson → MyMod/json/ → Edit值 → fromjson → MyMod/files/ → UnrealPak打包 → MyMod/pak/ → cp到游戏Paks/
```

每一步：

1. **查对照表**：`建筑中英对照表.txt` 找中文名→目录名
2. **cp源文件**：从 `_game_extract/Tropico6/Content/Blueprints/Buildings/<目录>/` 到 `MyMod/files/Blueprints/Buildings/<目录>/`
3. **tojson**：`./UAssetGUI.exe tojson "源文件.uasset" "MyMod/json/XXX.json" 26`
4. **Edit JSON**：`DamagePerWorker` 里的 `RangeMin`/`RangeMax` 是伤害范围
5. **fromjson**：`./UAssetGUI.exe fromjson "MyMod/json/XXX.json" "MyMod/files/.../XXX.uasset"`
6. **打包**：见上方绝对路径铁律
7. **部署**：`cp MyMod/pak/z_MyMod.pak "游戏Paks目录/z_MyMod.pak"`，同时删旧的 `z_Watchtower.pak`

## 避坑

- 必须用本机游戏提取的 V21 文件，网上旧版文件会导致鼠标悬停就闪退（EXCEPTION_ACCESS_VIOLATION）
- 提取游戏 pak 加 `-Filter="*关键词*"` 能秒出结果，别全量解包单文件
- 属性里 `DamagePerWorker` 是 `T6Range` 结构体，值在嵌套的 `RangeMin`/`RangeMax` 里，别改外层
- `JobCapacity` 类型是 `Byte`，值超过 255 会截断
