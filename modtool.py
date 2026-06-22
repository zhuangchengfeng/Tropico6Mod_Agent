#!/usr/bin/env python3
"""
Tropico 6 Modding CLI — 一站式模组管理工具
用法: python modtool.py <命令> [参数...]
"""

import json, os, sys, subprocess, shutil, re, glob, struct

# ============================================================
# 路径配置
# ============================================================
ROOT       = r"E:\Tropico6Modding"
SRC        = os.path.join(ROOT, "_game_extract/Tropico6/Content/Blueprints/Buildings")
JSON_DIR   = os.path.join(ROOT, "MyMod/json")
FILES_DIR  = os.path.join(ROOT, "MyMod/files/Blueprints/Buildings")
PAK_PATH   = os.path.join(ROOT, "MyMod/pak/z_MyMod.pak")
PATH_TXT   = os.path.join(ROOT, "_path.txt")
GAME_PAKS  = r"C:/TP6/Tropico 6/Tropico6/Content/Paks"
MAP_FILE   = os.path.join(ROOT, "建筑中英对照表.txt")
UASSET_GUI = os.path.join(ROOT, "UAssetGUI.exe")
UNREAL_PAK = os.path.join(ROOT, "UnrealPakTool/UnrealPak[v5_UE4.20].exe")
FINISH_PAKS = os.path.join(ROOT, "finish_paks")
MY_MODS_DIR = os.path.join(ROOT, "_my_mods")

# ============================================================
# 工具函数
# ============================================================
def load_json(name):
    """加载 MyMod/json/<name>.json"""
    if not name.endswith(".json"):
        name += ".json"
    path = os.path.join(JSON_DIR, name)
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_json(name, data):
    """保存到 MyMod/json/<name>.json"""
    if not name.endswith(".json"):
        name += ".json"
    with open(os.path.join(JSON_DIR, name), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def json_names():
    """列出所有 JSON 文件名（不含 .bak）"""
    return sorted(f for f in os.listdir(JSON_DIR) if f.endswith(".json") and ".bak" not in f)

def walk_data(obj, callback):
    """递归遍历 JSON 导出数据，对每个有 Name 的 dict 调用 callback(name, value_dict)"""
    if isinstance(obj, dict):
        if "Name" in obj and isinstance(obj["Name"], str):
            callback(obj)
        for v in obj.values():
            walk_data(v, callback)
    elif isinstance(obj, list):
        for item in obj:
            walk_data(item, callback)

def find_uasset(json_name):
    """在 MyMod/files/ 中查找 json 对应的 uasset 路径"""
    uasset = json_name.replace(".json", ".uasset") if json_name.endswith(".json") else json_name + ".uasset"
    for root, _, files in os.walk(FILES_DIR):
        if uasset in files:
            return os.path.join(root, uasset)
    return None

def find_src_uasset(name):
    """在 _game_extract 中查找 uasset 文件"""
    uasset = name if name.endswith(".uasset") else name + ".uasset"
    for root, _, files in os.walk(SRC):
        if uasset in files:
            return os.path.join(root, uasset)
    return None

def run(cmd, silent=False):
    """执行命令并返回 (returncode, stdout, stderr)"""
    r = subprocess.run(cmd, capture_output=True, text=True, shell=False)
    if not silent or r.returncode != 0:
        if r.stdout.strip():
            print(r.stdout.strip())
        if r.stderr.strip():
            print(r.stderr.strip(), file=sys.stderr)
    return r.returncode, r.stdout, r.stderr

def get_custom_mods():
    """扫描 _my_mods/ 获取自定义 mod 列表，返回 [(name, folder_path, path_file)]"""
    mods = []
    if not os.path.exists(MY_MODS_DIR):
        return mods
    for name in sorted(os.listdir(MY_MODS_DIR)):
        path = os.path.join(MY_MODS_DIR, name)
        if name == "_path" or name.startswith("."):
            continue
        if os.path.isdir(path):
            pfile = os.path.join(MY_MODS_DIR, "_path", f"_path_{name}.txt")
            if os.path.exists(pfile):
                mods.append((name, path, pfile))
    return mods

def get_pak_name(mod_name):
    """自定义 mod 文件夹名 → pak 文件名"""
    return f"z_{mod_name}.pak"

# ============================================================
# 搜索映射
# ============================================================
def load_map():
    """加载 建筑中英对照表.txt → {中文名: 英文目录}"""
    mapping = {}
    if os.path.exists(MAP_FILE):
        with open(MAP_FILE, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "|" in line:
                    cn, en = line.split("|", 1)
                    mapping[cn.strip()] = en.strip()
    return mapping

# ============================================================
# 命令实现
# ============================================================
def cmd_find(args):
    """搜索建筑中文名"""
    if not args:
        print("用法: modtool find <关键词>")
        return
    kw = args[0].lower()
    mapping = load_map()
    found = [(cn, en) for cn, en in mapping.items() if kw in cn.lower() or kw in en.lower()]
    if not found:
        print(f"没找到匹配「{kw}」的建筑")
        return
    for cn, en in found[:30]:
        print(f"  {cn:20s} | {en}")
    if len(found) > 30:
        print(f"  ... 还有 {len(found)-30} 条结果")

def cmd_info(args):
    """精简展示 JSON 属性"""
    if not args:
        # 没有参数则列出所有 JSON
        for n in json_names():
            print(f"  {n}")
        return
    d = load_json(args[0])
    print(f"=== {args[0]} ===")
    seen = set()
    def show(obj):
        n = obj.get("Name", "")
        if not n or n in seen:
            return
        seen.add(n)
        v = obj.get("Value")
        if isinstance(v, (int, float, str, bool)):
            print(f"  {n} = {v}")
        elif isinstance(v, list) and len(v) <= 2:
            # Nested structure — show sub-items
            for sub in v:
                if isinstance(sub, dict) and "Name" in sub:
                    print(f"    {sub['Name']} = {sub.get('Value','?')}")
    exports = d.get("Exports", [])
    for exp in exports:
        if isinstance(exp, dict):
            walk_data(exp, show)

def cmd_detail(args):
    """完整展示 JSON 属性（含嵌套）"""
    if not args:
        print("用法: modtool detail <json名>")
        return
    d = load_json(args[0])
    print(f"=== {args[0]} ===")
    def show(obj, depth=0):
        indent = "  " * depth
        if isinstance(obj, dict):
            if "Name" in obj and isinstance(obj["Name"], str):
                v = obj.get("Value", "?")
                if isinstance(v, (str, int, float, bool)):
                    print(f"{indent}{obj['Name']} = {v}")
                elif isinstance(v, list):
                    print(f"{indent}{obj['Name']} = [")
                    for item in v:
                        if isinstance(item, dict) and "Name" in item:
                            show(item, depth + 1)
                    print(f"{indent}]")
                else:
                    print(f"{indent}{obj['Name']} = <{type(v).__name__}>")
            for k, val in obj.items():
                show(val, depth + 1)
        elif isinstance(obj, list):
            for item in obj:
                show(item, depth)
    exports = d.get("Exports", [])
    for exp in exports:
        if isinstance(exp, dict):
            show(exp)

def cmd_set(args):
    """修改 JSON 中某个属性的值"""
    if len(args) < 2:
        print("用法: modtool set <json名> <属性名> [值]")
        print("  例: modtool set BP_Prison DetentionSlots 255")
        print("  例: modtool set BP_ColonialGuardTower RangeMin 1000.0")
        return
    jname, pname = args[0], args[1]
    new_val = args[2] if len(args) > 2 else None

    d = load_json(jname)
    found = []

    def collect(obj):
        if isinstance(obj, dict) and obj.get("Name") == pname:
            found.append(obj)

    exports = d.get("Exports", [])
    for exp in exports:
        if isinstance(exp, dict):
            walk_data(exp, collect)

    if not found:
        # 再搜一次外层（Exports 层的 Data）
        for exp in exports:
            if isinstance(exp, dict) and isinstance(exp.get("Data"), list):
                for item in exp["Data"]:
                    if isinstance(item, dict) and item.get("Name") == pname:
                        found.append(item)
        if not found:
            print(f"未找到属性「{pname}」")
            return

    if new_val is None:
        # 只读取，不修改
        for f in found:
            print(f"  {f['Name']} = {f.get('Value', '?')}")
        return

    # 修改
    for f in found:
        old = f.get("Value")
        # 类型推断
        if isinstance(old, bool):
            new_val_typed = new_val.lower() in ("true", "1", "yes")
        elif "." in str(new_val):
            new_val_typed = float(new_val)
        elif isinstance(old, int):
            new_val_typed = int(new_val)
        else:
            new_val_typed = new_val
        f["Value"] = new_val_typed
        print(f"  {f['Name']}: {old} → {new_val_typed}")

    save_json(jname, d)
    print(f"  已保存 {jname}")

def cmd_tojson(args):
    """uasset → json"""
    if len(args) < 2:
        print("用法: modtool tojson <源uasset路径相对于Blueprints/Buildings/> <json名>")
        print("  例: modtool tojson WorldWars/Prison/BP_Prison BP_Prison")
        return
    rel_path = args[0]
    src_uasset = os.path.join(SRC, rel_path) if not os.path.isabs(rel_path) else rel_path
    if not src_uasset.endswith(".uasset"):
        src_uasset += ".uasset"
    jname = args[1]
    dst_json = os.path.join(JSON_DIR, jname if jname.endswith(".json") else jname + ".json")

    if os.path.exists(dst_json):
        print(f"⚠ {jname} 已存在，跳过（不要重复 tojson）")
        return
    run([UASSET_GUI, "tojson", src_uasset, dst_json, "26"])

def cmd_fromjson(args):
    """json → uasset+uexp"""
    if not args:
        print("用法: modtool fromjson <json名> [输出路径]")
        print("  例: modtool fromjson BP_Prison")
        return
    jname = args[0]
    jpath = os.path.join(JSON_DIR, jname if jname.endswith(".json") else jname + ".json")
    if not os.path.exists(jpath):
        print(f"JSON 文件不存在: {jpath}")
        return

    if len(args) > 1:
        dst = args[1]
    else:
        dst = find_uasset(jname)
        if not dst:
            print(f"未在 MyMod/files/ 中找到 {jname} 对应的 uasset，请提供完整路径")
            return
    run([UASSET_GUI, "fromjson", jpath, dst])

def cmd_cp(args):
    """拷贝源文件"""
    if not args:
        print("用法: modtool cp <英文目录路径>")
        print("  例: modtool cp WorldWars/Prison/BP_Prison")
        print("  例: modtool cp 警卫塔  （通过中文名查找）")
        return

    name = args[0]
    # 先查对照表
    mapping = load_map()
    for cn, en in mapping.items():
        if name in cn:
            name = en
            break

    src = find_src_uasset(name)
    if not src:
        print(f"未在 _game_extract/ 中找到 {name}")
        return

    # 计算目标路径
    rel = os.path.relpath(src, SRC)
    dst_uasset = os.path.join(FILES_DIR, rel)
    dst_uexp = dst_uasset.replace(".uasset", ".uexp")
    os.makedirs(os.path.dirname(dst_uasset), exist_ok=True)

    shutil.copy2(src, dst_uasset)
    src_uexp = src.replace(".uasset", ".uexp")
    if os.path.exists(src_uexp):
        shutil.copy2(src_uexp, dst_uexp)
    print(f"  已拷贝 → {rel}")

def cmd_convert(args):
    """一键：查表→cp→tojson"""
    if not args:
        print("用法: modtool convert <中文建筑名或英文目录>")
        print("  例: modtool convert 监狱")
        return
    name = args[0]
    mapping = load_map()
    eng = name
    for cn, en in mapping.items():
        if name in cn:
            eng = en
            print(f"  中文→英文: {cn} → {en}")
            break

    # 找到源文件
    src = find_src_uasset(eng)
    if not src:
        print(f"  未找到 {eng}，尝试子目录搜索...")
        # 搜索匹配的目录
        for root, dirs, _ in os.walk(SRC):
            for d in dirs:
                if eng.lower() in d.lower():
                    # 找主蓝图文件
                    subdir = os.path.join(root, d)
                    for f in os.listdir(subdir):
                        if f.endswith(".uasset") and "Placement" not in f and "Visual" not in f and "Upgrade" not in f and "Workmode" not in f:
                            src = os.path.join(subdir, f)
                            eng = os.path.relpath(src, SRC)
                            break
                    break
        if not src:
            print(f"  未找到 {name}")
            return

    print(f"  源文件: {src}")

    # cp
    rel = os.path.relpath(src, SRC)
    dst_uasset = os.path.join(FILES_DIR, rel)
    dst_uexp = dst_uasset.replace(".uasset", ".uexp")
    os.makedirs(os.path.dirname(dst_uasset), exist_ok=True)
    shutil.copy2(src, dst_uasset)
    src_uexp = src.replace(".uasset", ".uexp")
    if os.path.exists(src_uexp):
        shutil.copy2(src_uexp, dst_uexp)

    # tojson
    jname = os.path.basename(src).replace(".uasset", "")
    jpath = os.path.join(JSON_DIR, jname + ".json")
    if os.path.exists(jpath):
        print(f"  JSON 已存在，跳过 tojson → {jname}.json")
    else:
        run([UASSET_GUI, "tojson", src, jpath, "26"])
        print(f"  已转换 → {jname}.json")

def cmd_stock(args):
    """批量修改库存和生产率"""
    capacity = 30000.0
    rate = 10.0
    for a in args:
        if a.startswith("--capacity="):
            capacity = float(a.split("=")[1])
        elif a.startswith("--rate="):
            rate = float(a.split("=")[1])

    total = 0
    for jname in json_names():
        d = load_json(os.path.basename(jname))
        file_count = [0]

        def mod_stock(obj):
            if isinstance(obj, dict):
                if obj.get("Name") in ("InStocksData", "OutStocksData") and isinstance(obj.get("Value"), list):
                    for stock in obj["Value"]:
                        if isinstance(stock, dict) and isinstance(stock.get("Value"), list):
                            for prop in stock["Value"]:
                                if isinstance(prop, dict):
                                    if prop.get("Name") == "Capacity" and isinstance(prop.get("Value"), (int, float)) and 0 < prop["Value"] < 100000:
                                        prop["Value"] = capacity
                                        file_count[0] += 1
                                    if prop.get("Name") == "ProductionRate" and isinstance(prop.get("Value"), (int, float)) and prop["Value"] > 0:
                                        prop["Value"] = rate
                for v in obj.values():
                    mod_stock(v)
            elif isinstance(obj, list):
                for item in obj:
                    mod_stock(item)

        exports = d.get("Exports", [])
        for exp in exports:
            if isinstance(exp, dict):
                mod_stock(exp)

        if file_count[0] > 0:
            save_json(jname, d)
            total += file_count[0]

    print(f"  已修改 {total} 处")
    print(f"  库存 → {capacity}, 生产率 → {rate}")
    print("  提示: 运行 'python modtool.py full' 一键打包部署")

def cmd_housing(args):
    """批量翻倍住宅容量"""
    multi = 2.0
    for a in args:
        if a.startswith("--multiplier="):
            multi = float(a.split("=")[1])

    housing = ["BP_Apartment","BP_T6CountryHouse","BP_T6Bunkhouse","BP_T6Flophouse",
               "BP_T6Tenement","BP_T6Conventillo","BP_T6ModernApartment"]
    for jname in housing:
        jpath = os.path.join(JSON_DIR, jname + ".json")
        if not os.path.exists(jpath):
            continue
        d = load_json(jname)
        exports = d.get("Exports", [])

        def mod_housing(obj):
            if isinstance(obj, dict) and obj.get("Name") == "HouseholdCapacity":
                old = obj.get("Value", 0)
                if isinstance(old, (int, float)) and old > 0:
                    obj["Value"] = int(old * multi)
                    return old, obj["Value"]
            if isinstance(obj, dict):
                for v in obj.values():
                    r = mod_housing(v)
                    if r: return r
            elif isinstance(obj, list):
                for item in obj:
                    r = mod_housing(item)
                    if r: return r
            return None

        for exp in exports:
            if isinstance(exp, dict):
                result = mod_housing(exp)
                if result:
                    print(f"  {jname}: HouseholdCapacity {result[0]} → {result[1]}")

        save_json(jname, d)

def cmd_fromjson_all(args):
    """将所有 JSON 转回 uasset"""
    ok = 0
    for jname in json_names():
        dst = find_uasset(jname)
        if not dst:
            continue
        rc, _, _ = run([UASSET_GUI, "fromjson", os.path.join(JSON_DIR, jname), dst], silent=True)
        if rc == 0:
            ok += 1
        else:
            print(f"  FAIL: {jname}")
    print(f"  OK {ok}/{len(json_names())}")

def cmd_package(args):
    """打包所有 mod 到 finish_paks/"""
    os.makedirs(FINISH_PAKS, exist_ok=True)
    total = 0

    # 1. 打包 MyMod（主 mod）
    print("--- z_MyMod (主 mod) ---")
    need_fromjson = False
    for jname in json_names():
        ua = find_uasset(jname)
        if ua and os.path.exists(ua):
            jtime = os.path.getmtime(os.path.join(JSON_DIR, jname))
            utime = os.path.getmtime(ua)
            if jtime > utime:
                need_fromjson = True
                break
        elif ua:
            need_fromjson = True
            break

    if need_fromjson:
        print("  检测到 JSON 比 uasset 新，先运行 fromjson-all...")
        cmd_fromjson_all([])
        apply_hex_patches()
    else:
        apply_hex_patches()

    # 写 _path.txt
    content = f'"{ROOT}\\MyMod\\files\\*" "../../../Tropico6/Content/"'
    with open(PATH_TXT, "w") as f:
        f.write(content)

    mymod_pak = os.path.join(FINISH_PAKS, "z_MyMod.pak")
    rc, out, err = run([UNREAL_PAK, mymod_pak, f"-Create={PATH_TXT}", "-compress"])
    if rc == 0:
        size = os.path.getsize(mymod_pak)
        nfiles = int(re.search(r"Added (\d+) files", out).group(1)) if "Added" in out else "?"
        print(f"  OK: {nfiles} 文件, {size/1024:.0f}KB\n")
        total += 1
    else:
        print(f"  FAIL\n")

    # 2. 打包自定义 mod（_my_mods/）
    custom_mods = get_custom_mods()
    for mod_name, mod_path, path_file in custom_mods:
        print(f"--- z_{mod_name} ---")
        pak_path = os.path.join(FINISH_PAKS, f"z_{mod_name}.pak")
        rc, out, err = run([UNREAL_PAK, pak_path, f"-Create={path_file}", "-compress"])
        if rc == 0:
            size = os.path.getsize(pak_path)
            nfiles = int(re.search(r"Added (\d+) files", out).group(1)) if "Added" in out else "?"
            print(f"  OK: {nfiles} 文件, {size/1024:.0f}KB\n")
            total += 1
        else:
            print(f"  FAIL\n")

    print(f"全部完成: {total} 个 pak → {FINISH_PAKS}")

def cmd_deploy(args):
    """部署所有 pak 到游戏目录"""
    if not os.path.exists(FINISH_PAKS):
        print("  finish_paks/ 不存在，先运行 package")
        return
    paks = [f for f in os.listdir(FINISH_PAKS) if f.endswith(".pak")]
    if not paks:
        print("  finish_paks/ 中没有 pak 文件")
        return
    for f in sorted(paks):
        src = os.path.join(FINISH_PAKS, f)
        dst = os.path.join(GAME_PAKS, f)
        shutil.copy2(src, dst)
        size = os.path.getsize(src)
        print(f"  {f} → {dst}  ({size/1024:.0f}KB)")
    print(f"  已部署 {len(paks)} 个 pak")

def cmd_status(args):
    """展示当前 mod 状态"""
    n_json = len(json_names())
    n_uasset = sum(1 for _ in os.walk(FILES_DIR) for f in _[2] if f.endswith(".uasset"))
    pak_size = os.path.getsize(PAK_PATH) if os.path.exists(PAK_PATH) else 0

    print(f"  JSON 文件:  {n_json}")
    print(f"  uasset 文件: {n_uasset}")
    print(f"  pak 大小:   {pak_size/1024/1024:.2f}MB")

    # 自定义 mod
    custom = get_custom_mods()
    if custom:
        print(f"\n  自定义 mod ({len(custom)}):")
        for name, path, _ in custom:
            nf = sum(1 for _ in os.walk(path) for f in _[2])
            print(f"    {name}: {nf} 文件")

    # finish_paks
    if os.path.exists(FINISH_PAKS):
        paks = [f for f in os.listdir(FINISH_PAKS) if f.endswith(".pak")]
        if paks:
            print(f"\n  finish_paks ({len(paks)}):")
            for f in sorted(paks):
                fp = os.path.join(FINISH_PAKS, f)
                print(f"    {f} ({os.path.getsize(fp)/1024:.0f}KB)")

    # 列出最近修改的 JSON
    print(f"\n  修改历史（最新 10）:")
    files_with_time = []
    for jname in json_names():
        mtime = os.path.getmtime(os.path.join(JSON_DIR, jname))
        files_with_time.append((mtime, jname))
    files_with_time.sort(reverse=True)
    from datetime import datetime
    for mtime, jname in files_with_time[:10]:
        dt = datetime.fromtimestamp(mtime).strftime("%m-%d %H:%M")
        print(f"    {dt}  {jname}")

# ============================================================
# Hex Patches — fromjson 无法写入 FloatProperty/ByteProperty
# 在 fromjson-all 之后自动执行
# ============================================================
HEX_PATCHES = [
    # LooseLoadLimit: MaximumLoss 10→0
    ("Blueprints/Buildings/Colonial/TeamstersOffice/BP_T6WorkmodeLooseLoadLimit.uexp", 10, 0, "int", "MaxLoss 10→0"),
    # LooseLoadLimit: TeamsterCapacityModifierPercent 1.5→10.0
    ("Blueprints/Buildings/Colonial/TeamstersOffice/BP_T6WorkmodeLooseLoadLimit.uexp", 1.5, 10.0, "float", "CapMod 1.5→10.0"),
    # Teamster: MovementSpeed 1200→6000 + RotationSpeed 180→900
    ("Blueprints/AgentMovementData/BP_TeamsterMovementData.uexp", 1200.0, 6000.0, "float", "Speed 1200→6000"),
    ("Blueprints/AgentMovementData/BP_TeamsterMovementData.uexp", 180.0, 900.0, "float", "Rotation 180→900"),
    ("Blueprints/AgentMovementData/BP_EmptyTeamsterMovementData.uexp", 1200.0, 6000.0, "float", "Speed 1200→6000"),
    ("Blueprints/AgentMovementData/BP_EmptyTeamsterMovementData.uexp", 180.0, 900.0, "float", "Rotation 180→900"),
]

def apply_hex_patches():
    """在 MyMod/files/ 中搜索 uexp 并应用 hex-patches"""
def apply_hex_patches():
    """在 MyMod/files/ 中搜索 uexp 并应用 hex-patches，如目标文件不存在则从源拷贝"""
    files_root = os.path.join(ROOT, "MyMod/files")
    src_root   = os.path.join(ROOT, "_game_extract/Tropico6/Content")
    patched = 0

    for rel_path, old_val, new_val, val_type, desc in HEX_PATCHES:
        dst = os.path.join(files_root, rel_path)
        src = os.path.join(src_root, rel_path)

        # 目标不存在 → 从源拷贝
        if not os.path.exists(dst):
            if not os.path.exists(src):
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src.replace(".uexp", ".uasset"), dst.replace(".uexp", ".uasset"))
            shutil.copy2(src, dst)

        data = bytearray(open(dst, "rb").read())
        old_bytes = struct.pack("<i", old_val) if val_type == "int" else struct.pack("<f", old_val)
        new_bytes = struct.pack("<i", new_val) if val_type == "int" else struct.pack("<f", new_val)

        pos = data.find(old_bytes, 0x50 if "LooseLoad" in rel_path else 0)
        if pos >= 0:
            data[pos:pos+4] = new_bytes
            open(dst, "wb").write(data)
            patched += 1

    if patched:
        print(f"  Hex patch: {patched}/{len(HEX_PATCHES)} 处已修补")

def cmd_hexpatch(args):
    """手动执行 hex-patches"""
    apply_hex_patches()
    print("  完成")

def cmd_full(args):
    """一键 fromjson-all + package + deploy"""
    cmd_fromjson_all([])
    print()
    apply_hex_patches()
    print()
    cmd_package([])
    print()
    cmd_deploy([])

# ============================================================
# 命令路由
# ============================================================
COMMANDS = {
    "find":          cmd_find,
    "info":          cmd_info,
    "detail":        cmd_detail,
    "set":           cmd_set,
    "tojson":        cmd_tojson,
    "fromjson":      cmd_fromjson,
    "cp":            cmd_cp,
    "convert":       cmd_convert,
    "stock":         cmd_stock,
    "housing":       cmd_housing,
    "fromjson-all":  cmd_fromjson_all,
    "hexpatch":      cmd_hexpatch,
    "package":       cmd_package,
    "deploy":        cmd_deploy,
    "status":        cmd_status,
    "full":          cmd_full,
}

USAGE = """modtool.py — Tropico6 模组工具

命令:
  find    <关键词>       搜索建筑对表
  info    [json名]       展示属性（无参数则列出所有 JSON）
  detail  <json名>       展示属性（含完整嵌套）
  set     <json> <属性> [值]  读取/修改属性
  tojson  <源路径> <名>     uasset→json (仅首次)
  fromjson <json> [路径]  json→uasset
  cp      <建筑名>        拷贝源文件
  convert <建筑名>        一键查表+cp+tojson
  stock   [--capacity=N] [--rate=N]  批量改库存/生产率
  housing [--multiplier=N]           批量翻倍住宅容量
  fromjson-all           全部 json→uasset
  hexpatch               修复 fromjson 遗漏的 FloatProperty
  package                打包
  deploy                 部署到游戏
  full                   fromjson-all + package + deploy
  status                 查看当前状态

示例:
  modtool find 警卫塔
  modtool convert 监狱
  modtool set BP_Prison DetentionSlots 255
  modtool package && modtool deploy"""

def main():
    if len(sys.argv) < 2:
        print(USAGE)
        return
    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd in COMMANDS:
        COMMANDS[cmd](args)
    elif cmd in ("-h", "--help", "help"):
        print(USAGE)
    else:
        print(f"未知命令: {cmd}")
        print(f"可用命令: {', '.join(COMMANDS)}")

if __name__ == "__main__":
    main()
