"""
批量修改公共服务和娱乐建筑
- 就业2x, 服务人数2x
- 娱乐建筑: 游客服务2x
"""
import json, os, subprocess

SRC = "_game_extract/Tropico6/Content/Blueprints/Buildings"
JSON_DIR = "MyMod/json"
UASSET_GUI = "./UAssetGUI.exe"

# 公共服务: 就业2x, 服务2x
PUBLIC_SERVICE = {
    "WorldWars/Hospital": ("BP_T6Hospital", "Hospital"),
    "WorldWars/Grocery": ("BP_Grocery", "Grocery"),
    "Colonial/Tavern": ("BP_Tavern", "Tavern"),
    "Colonial/Restaurant": ("BP_Restaurant", "Restaurant"),
}

# 娱乐和奢侈娱乐: 游客服务2x
ENTERTAINMENT = {
    "ColdWar/Casino": ("BP_T6Casino", "Casino"),
    "ColdWar/NightClub": ("BP_T6NightClub", "NightClub"),
    "ColdWar/MovieTheater": ("BP_T6MovieTheater", "MovieTheater"),
    "ColdWar/GourmetRestaurant": ("BP_T6GourmetRestaurant", "Gourmet"),
    "ColdWar/GolfCourse": ("BP_T6GolfCourse", "Golf"),
    "ColdWar/BeachVilla": ("BP_T6BeachVilla", "BeachVilla"),
    "Colonial/Circus": ("BP_Circus", "Circus"),
    "Colonial/Theater": ("BP_Theater", "Theater"),
    "WorldWars/Cabaret": ("BP_Cabaret", "Cabaret"),
    "ModernTimes/Stadium": ("BP_T6Stadium", "Stadium"),
    "ModernTimes/BeachResort": ("BP_T6BeachResort", "BeachResort"),
    "ModernTimes/MuseumOfModernArt": ("BP_T6MuseumOfModernArt", "Museum"),
    "ColdWar/ChildhoodMuseum": ("BP_T6ChildhoodMuseum", "ChildMuseum"),
    "DLC/Future/SpacePort": ("BP_T6SpacePort", "SpacePort"),
    "DLC/Future/SpacePortComplex": ("BP_T6SpacePortComplex", "SpacePortComplex"),
}

# 货车办公室: 就业2x
TEAMSTER = {"Colonial/TeamstersOffice/BP_Building_Teamster": "BP_Building_Teamster"}

FILES_DIR = "MyMod/files/Blueprints/Buildings"

def convert_and_check(path, uasset_name, label):
    """Convert to JSON if not exists, return properties"""
    src = os.path.join(SRC, path, uasset_name + ".uasset")
    if not os.path.exists(src):
        return None
    jpath = os.path.join(JSON_DIR, uasset_name + ".json")
    if not os.path.exists(jpath):
        subprocess.run([UASSET_GUI, "tojson", src, jpath, "26"], capture_output=True)
    return jpath

modified = []

# Process Hospital, Grocery, Tavern
for path, (uasset, label) in PUBLIC_SERVICE.items():
    jpath = convert_and_check(path, uasset, label)
    if not jpath:
        continue
    d = json.load(open(jpath, encoding="utf-8"))
    chg = [False]

    def walk(obj):
        if isinstance(obj, dict):
            n = obj.get("Name")
            # JobCapacity x2
            if n == "JobCapacity" and isinstance(obj.get("Value"), int) and obj["Value"] > 0:
                obj["Value"] = obj["Value"] * 2
                chg[0] = True
            # Visitor/Service capacity x2
            if n in ("VisitorsPerWorker", "ServiceCapacity", "VisitorCapacity") and isinstance(obj.get("Value"), (int, float)) and obj["Value"] > 0:
                obj["Value"] = obj["Value"] * 2
                chg[0] = True
            if n == "BaseServiceQuality" and isinstance(obj.get("Value"), (int, float)) and obj["Value"] > 0:
                obj["Value"] = 100  # max quality
                chg[0] = True
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    for exp in d.get("Exports", []):
        if isinstance(exp, dict):
            walk(exp)

    if chg[0]:
        with open(jpath, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"  {label}: 就业2x + 服务2x")

# Process entertainment buildings
print("\n=== Entertainment (visitor service 2x) ===")
for path, (uasset, label) in ENTERTAINMENT.items():
    jpath = convert_and_check(path, uasset, label)
    if not jpath:
        print(f"  {label}: NOT FOUND")
        continue
    d = json.load(open(jpath, encoding="utf-8"))
    chg = [False]

    def walk(obj):
        if isinstance(obj, dict):
            n = obj.get("Name")
            if n in ("VisitorsPerWorker", "VisitorCapacity", "GuestCapacity", "ServiceCapacity") and isinstance(obj.get("Value"), (int, float)) and obj["Value"] > 0:
                obj["Value"] = obj["Value"] * 2
                chg[0] = True
            if n == "JobCapacity" and isinstance(obj.get("Value"), int) and obj["Value"] > 0:
                obj["Value"] = obj["Value"] * 2
                chg[0] = True
            if n == "BaseServiceQuality" and isinstance(obj.get("Value"), (int, float)) and obj["Value"] > 0:
                obj["Value"] = min(obj["Value"] * 2, 100)
                chg[0] = True
            for v in obj.values():
                walk(v)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)

    for exp in d.get("Exports", []):
        if isinstance(exp, dict):
            walk(exp)

    if chg[0]:
        with open(jpath, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        print(f"  {label}: service 2x + job 2x")

print("\nDone!")
