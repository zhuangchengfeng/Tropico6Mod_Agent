"""Remove build limit from all world wonders / landmarks"""
import json, os, subprocess

SRC = "_game_extract/Tropico6/Content/Blueprints/Buildings/BuildingData"
JSON_DIR = "MyMod/json"
FILES_DIR = "MyMod/files/Blueprints/Buildings/BuildingData"
UASSET_GUI = "./UAssetGUI.exe"

landmarks = [
    ("Colonial/DA_T6BrandenburgGateBP.uasset", "Brandenburg Gate"),
    ("Colonial/DA_T6HagiaSophiaBP.uasset", "Hagia Sophia"),
    ("ColdWar/DA_T6Colosseum.uasset", "Colosseum"),
    ("ColdWar/DA_T6GreatSphinx.uasset", "Great Sphinx"),
    ("ColdWar/DA_T6StatueOfLiberty.uasset", "Statue of Liberty"),
    ("WorldWars/DA_AhuAkiviMoaiHeads.uasset", "Moai Heads"),
    ("WorldWars/DA_T6TajMahal.uasset", "Taj Mahal"),
    ("WorldWars/DA_T6EiffelTower.uasset", "Eiffel Tower"),
    ("ModernTimes/DA_WinterPalace.uasset", "Winter Palace"),
]

for rel, name in landmarks:
    src = os.path.join(SRC, rel)
    if not os.path.exists(src):
        print(f"  {name}: NOT FOUND")
        continue

    jname = os.path.basename(rel).replace(".uasset", ".json")
    jpath = os.path.join(JSON_DIR, jname)

    # Convert
    result = subprocess.run([UASSET_GUI, "tojson", src, jpath, "26"], capture_output=True, text=True)
    if result.returncode != 0:
        continue

    d = json.load(open(jpath, encoding="utf-8"))
    chg = False

    for exp in d.get("Exports", []):
        if isinstance(exp, dict) and isinstance(exp.get("Data"), list):
            for item in exp["Data"]:
                if isinstance(item, dict) and item.get("Name") == "DefaultAmountBuildable":
                    old = item["Value"]
                    # Change One/Disabled -> OneOrMore
                    if "One" in str(old) or "Disabled" in str(old):
                        item["Value"] = "ET6BuildingAmountType::OneOrMore"
                        chg = True
                        print(f"  {name}: {old} -> OneOrMore")

    if chg:
        with open(jpath, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)

        # Copy source files
        dst_dir = os.path.dirname(os.path.join(FILES_DIR, rel))
        os.makedirs(dst_dir, exist_ok=True)
        src_uexp = src.replace(".uasset", ".uexp")
        import shutil
        shutil.copy2(src, os.path.join(FILES_DIR, rel))
        if os.path.exists(src_uexp):
            shutil.copy2(src_uexp, os.path.join(FILES_DIR, rel.replace(".uasset", ".uexp")))

        # fromjson
        subprocess.run([UASSET_GUI, "fromjson", jpath, os.path.join(FILES_DIR, rel)], capture_output=True)

print("Done!")
