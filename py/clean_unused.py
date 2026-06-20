"""删除未修改的 JSON 和对应的 MyMod/files/ 源文件"""
import os, json, shutil

JSON_DIR = "MyMod/json"
FILES_DIR = "MyMod/files"

# These patterns indicate a file was only converted for reading, not modified
# Modified JSONs have changed property values; unmodified are exact copies of source
UNUSED_PATTERNS = [
    # Animal blueprints (never modified)
    "BP_T6RanchAnimal",
    # Upgrade files (never modified)
    "BP_T6Upgrade", "BP_Upgrade",
    # Work modes (never modified, except specific ones)
    "BP_T6Workmode",
    "BP_Workmode",
    # Building data (never modified, except landmarks)
    "DA_T6Square", "DA_T6Storage",
    "DA_PowerPlant", "DA_NuclearPowerPlant",
    "DA_Prison", "DA_PoliceStation",
    "DA_Building_Teamster", "DA_T6Warehouse",
    "DA_ElectricSubstation",
    # Read-only temp
    "_temp_", "_fix_",
]

# Also keep specific work modes that WERE modified
KEEP_WORKMODES = [
    "BP_T6WorkmodeChannelOneTV.json",
]

keep_count = 0
delete_count = 0

# First pass: identify all JSONs
all_jsons = [f for f in os.listdir(JSON_DIR) if f.endswith(".json") and not f.endswith(".bak")]

for fname in all_jsons:
    should_delete = False

    # Check against unused patterns
    for pattern in UNUSED_PATTERNS:
        if pattern in fname:
            should_delete = True
            break

    # Don't delete work modes that should be kept
    if fname in KEEP_WORKMODES:
        should_delete = False

    if should_delete:
        jpath = os.path.join(JSON_DIR, fname)
        # Also remove .bak if exists
        bak = jpath + ".bak"
        if os.path.exists(bak):
            os.remove(bak)

        # Find and delete corresponding files in MyMod/files/
        uasset = fname.replace(".json", ".uasset")
        for root, _, files in os.walk(FILES_DIR):
            if uasset in files:
                upath = os.path.join(root, uasset)
                os.remove(upath)
                # Also remove .uexp
                upath_exp = upath.replace(".uasset", ".uexp")
                if os.path.exists(upath_exp):
                    os.remove(upath_exp)

        os.remove(jpath)
        delete_count += 1
        if delete_count <= 5:
            print(f"  DEL: {fname}")

if delete_count > 5:
    print(f"  ... and {delete_count - 5} more")

# Count remaining
remaining = [f for f in os.listdir(JSON_DIR) if f.endswith(".json") and not f.endswith(".bak")]
print(f"\nDeleted: {delete_count}, Remaining: {len(remaining)}")
for r in sorted(remaining):
    print(f"  {r}")
