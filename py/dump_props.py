"""提取建筑所有属性值，用于生成 mod.md"""
import json, os, sys

JSON_DIR = "MyMod/json"

def dump_all_props(jname):
    """返回 {属性名: 值} 字典"""
    jpath = os.path.join(JSON_DIR, jname)
    if not os.path.exists(jpath):
        return None
    d = json.load(open(jpath, encoding="utf-8"))
    props = {}
    ignores = {"ComponentClass","ComponentTemplate","VariableGuid","InternalVariableName",
               "DrivewayArrow","SelectionEv","UserFeedback","RootComponent","SimpleConstructionScript",
               "ObjectGuid","SerializationControl","Operation","HasLeadingFourNullBytes",
               "ObjectName","OuterIndex","ClassIndex","SuperIndex","TemplateIndex",
               "ObjectFlags","SerialSize","SerialOffset","PackageGuid","PackageFlags",
               "IsInheritedInstance","StructGUID","SerializeNone","SerializationControl",
               "RootNodes","AllNodes","DefaultSceneRootNode","BuildingIcon","BuildingIconByEra",
               "KeybindActionName","BuildingName","BuildingIntroduction","BuildingFlavorText",
               "BuildingEfficiencyDescription","BuildingClass","BlueprintCost","BlueprintCostOverwrite",
               "DefaultAmountBuildable","RequiredEra","BuildingCategory","HeistBuildingCategory",
               "PossibleWorkmodesList","PossibleUpgrades","AvailableBuildingInteractions",
               "BuildingPlacementClasses","BuildingPlacementClassesEraOverrides","buildingData",
               "ArchitectureStyle","InformationBuildingTexture","bParticleEffectsAllwaysOn",
               "SelectedBuildingPlacementData","bCanEverAffectNavigation","bReceivesDecals",
               "bGenerateOverlapEvents","StaticMesh","CanCharacterStepUpOn",
               "OccupationClassReference","WorkerEducation","BudgetLevelData",
               "bCallWorkerInstantlyToWorkDuringWar","bUpgradeSquadByEra","bDefensiveOnly",
               "ColonialSquadType","WorldWarSquadType","ModernSquadType",
               "KeybindActionName","EraUnlockData"}
    def walk(obj):
        if isinstance(obj, dict):
            n = obj.get("Name","")
            v = obj.get("Value")
            if n and not any(ign in n for ign in ignores) and not n.startswith("bCan") and not n.startswith("bIs") and not n.startswith("bReceives") and not n.startswith("bGenerate"):
                if isinstance(v, (str, int, float, bool)):
                    if isinstance(v, str) and ("::" in v or "/Game/" in v or len(v) > 40):
                        pass  # skip enum refs and long paths
                    else:
                        if n not in props:
                            props[n] = v
            for val in obj.values():
                walk(val)
        elif isinstance(obj, list):
            for item in obj:
                walk(item)
    for exp in d.get("Exports", []):
        if isinstance(exp, dict):
            walk(exp)
    return props

if len(sys.argv) > 1:
    for jname in sys.argv[1:]:
        props = dump_all_props(jname if jname.endswith(".json") else jname + ".json")
        if props:
            print(f"\n=== {jname} ===")
            for k, v in sorted(props.items()):
                print(f"  {k} = {v}")
else:
    print("用法: python dump_props.py <json名> [...]")
