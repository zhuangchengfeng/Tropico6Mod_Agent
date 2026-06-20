# MyMod 模组内容

---

## 警卫塔 ColonialGuardTower
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| DamagePerWorker.RangeMin | 1.4 | **500** | 最低攻击力 |
| DamagePerWorker.RangeMax | 2.6 | **500** | 最高攻击力 |
| ShotsBeforeReload | 1 | 1 | 换弹前射击次数 |
| AggroRange | 10 | **30** | 警戒范围(3x) |
| JobCapacity | 3 | 3 | 岗位数 |
| MonthlyWageBase | 7 | 7 | 月薪 |
| JobQualityBase | 40 | 40 | 岗位质量 |
| WorkDuration | 80 | 80 | 工作时长 |
| UpkeepBase | 2 | 2 | 维护费 |
| StructurePoints | 1800 | 1800 | 建筑血量 |
| GeneratorRadius (Liberty) | 8 | 8 | 自由覆盖半径 |
| GeneratorInfluence (Liberty) | -15 | -15 | 自由度影响 |
| GeneratorRadius (CrimeSafety) | 6 | 6 | 安保覆盖半径 |
| GeneratorInfluence (CrimeSafety) | 0 | 0 | 安保强度 |
| GeneratorRadius (MilitaryStrength) | 10 | 10 | 军事覆盖半径 |
| GeneratorInfluence (MilitaryStrength) | 15 | 15 | 军事影响力 |

---

## 警察局 PoliceStation
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| CriminalInterest | 0 | 0 | 犯罪兴趣度 |
| JobCapacity | 4 | 4 | 岗位数 |
| MonthlyWageBase | 8 | 8 | 月薪 |
| JobQualityBase | 60 | 60 | 岗位质量 |
| WorkDuration | 80 | 80 | 工作时长 |
| UpkeepBase | 2 | 2 | 维护费 |
| StructurePoints | 1600 | 1600 | 建筑血量 |
| bDefensiveOnly | True | True | 仅防御模式 |
| bUpgradeSquadByEra | True | True | 随时代升级小队 |
| GeneratorType | CrimeSafety | CrimeSafety | 覆盖类型：犯罪安全 |
| GeneratorShape | Sphere | Sphere | 覆盖形状：球形 |
| GeneratorRadius | 20 | **99999** | 安保覆盖半径，覆盖全图 |
| GeneratorCenterAxisLength | 0 | 0 | 中心轴长度 |
| GeneratorInfluence | 45 | **100** | 安保强度(安全度，最大值) |
| bScaledByEfficiency | False | False | 不随效率缩放 |
| GeneratorIntensityDropOffset | Drop0 | Drop0 | 边缘不衰减 |

---

## 监狱 Prison
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| CriminalInterest | 0 | 0 | 犯罪兴趣度 |
| DetentionSlots | 32 | **255** | 罪犯容量(Byte上限) |
| JobCapacity | 6 | 6 | 岗位数 |
| MonthlyWageBase | 10 | 10 | 月薪 |
| JobQualityBase | 50 | 50 | 岗位质量 |
| WorkDuration | 80 | 80 | 工作时长 |
| UpkeepBase | 50 | 50 | 维护费 |
| StructurePoints | 4000 | 4000 | 建筑血量 |
| GeneratorType | Liberty | Liberty | 覆盖类型：自由 |
| GeneratorShape | Sphere | Sphere | 覆盖形状 |
| GeneratorRadius | 7 | 7 | 覆盖半径 |
| GeneratorInfluence | -6 | -6 | 自由压制值 |

---

## 电视台 TVStation
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| CriminalInterest | 5 | 5 | 犯罪兴趣度 |
| ElectricityConsumption | 45 | 45 | 电力消耗 |
| InfluenceRange | 60 | **999999** | 影响范围，覆盖全图 |
| JobCapacity | 4 | 4 | 岗位数 |
| MonthlyWageBase | 20 | 20 | 月薪 |
| JobQualityBase | 70 | 70 | 岗位质量 |
| WorkDuration | 80 | 80 | 工作时长 |
| UpkeepBase | 60 | 60 | 维护费 |
| StructurePoints | 3700 | 3700 | 建筑血量 |
| bResidential | True | True | 属于住宅类 |
| bCheckHasElectricity | True | True | 需要电力 |
| bWorkplace | False | False | 非工作场所 |
| GeneratorType | Liberty | Liberty | 覆盖类型：自由 |
| GeneratorShape | Sphere | Sphere | 覆盖形状 |
| GeneratorRadius | 60 | **999999** | 自由覆盖半径，全图 |
| GeneratorInfluence | 15 | 15 | 自由度强度 |
| bScaledByEfficiency | True | True | 随效率缩放 |
| GeneratorIntensityDropOffset | Drop0 | Drop0 | 边缘不衰减 |

### 第一频道工作模式 ChannelOneTV
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| LibertyGeneratorDelta | -30 | **100** | 全图自由度 +100 |

---

## 大型广场 2x2 Square
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| GeneratorType | Beauty | Beauty | 覆盖类型：美观 |
| GeneratorShape | Sphere | Sphere | 覆盖形状 |
| GeneratorRadius | 5 | **99999** | 美观覆盖半径，全图 |
| GeneratorCenterAxisLength | 0 | 0 | 中心轴长度 |
| GeneratorInfluence | 14 | **100** | 美观度强度(最大值) |
| bScaledByEfficiency | False | False | 不随效率缩放 |
| GeneratorIntensityDropOffset | Drop0 | Drop0 | 边缘不衰减 |

---

## 垃圾填埋厂 GarbageDump
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| bShowDefaultInfluenceRange | True | True | 显示默认影响范围 |
| bPollutionEmitter | True | True | 污染排放者 |
| bGeneratePollutionIfNotOperational | True | **False** | 不工作时不再产生污染 |
| InfluenceRange | 30 | 30 | 影响范围 |
| CleansingRadius | 30 | **99999** | 净化半径，覆盖全图 |
| AbsolutePollutionDecrease | 0.01 | **100** | 污染降低值(最大值) |

---

## 变电站 ElectricSubstation
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| CriminalInterest | 0 | 0 | 犯罪兴趣度 |
| BuildingHasBudget | False | False | 无预算 |
| BuildingHasEfficiency | False | False | 无效率 |
| BuildingHasStatistics | False | False | 无统计 |
| ElectricityCellRadius | 60 | 60 | 电网单元半径 |
| ElectricityConsumption | 10 | 10 | 电力消耗 |
| InfluenceRange | 60 | **99999999** | 供电覆盖范围，全图 |
| PollutionIntensityCap | 0.25 | 0.25 | 污染强度上限 |
| PollutionRadius | 10 | 10 | 污染半径 |
| StructurePoints | 1300 | 1300 | 建筑血量 |
| ConstructionWorkerCapacity | 2 | 2 | 建造工人数 |
| bHomelessBuildShacksNearby | False | False | 无家可归者不在附近建棚屋 |
| bShouldDisplayWorldIcon | False | False | 不显示世界图标 |

---

## 地铁站 MetroStation
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| CriminalInterest | 5 | 5 | 犯罪兴趣度 |
| ElectricityConsumption | 20 | 20 | 电力消耗 |
| InfluenceRange | 10 | **999999** | 通勤覆盖范围，全图 |
| JobCapacity | 2 | **6** | 岗位数(3x) |
| MonthlyWageBase | 7 | 7 | 月薪 |
| JobQualityBase | 55 | 55 | 岗位质量 |
| WorkDuration | 90 | 90 | 工作时长 |
| UpkeepBase | 50 | 50 | 维护费 |
| StructurePoints | 1500 | 1500 | 建筑血量 |
| ConstructionWorkerCapacity | 4 | 4 | 建造工人数 |
| bResidential | True | True | 住宅类建筑 |
| bAccommodation | True | True | 提供住宿 |
| bWorkplace | False | False | 非工作场所 |
| GeneratorType | CrimeSafety | CrimeSafety | 覆盖类型：犯罪安全 |
| GeneratorShape | Sphere | Sphere | 覆盖形状 |
| GeneratorRadius | 4 | 4 | 安保覆盖半径 |
| GeneratorInfluence | -25 | -25 | 降低犯罪值 |

---

## 回收装置 Reclaimer (Future DLC)
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| CriminalInterest | 15 | 15 | 犯罪兴趣度 |
| ElectricityConsumption | 65 | 65 | 电力消耗 |
| InfluenceRange | 7.5 | **999999** | 回收覆盖范围，全图 |
| DefaultMaximumCapacityOfOutStock | 2000 | **30000** | 最大产出库存 |
| JobCapacity | 0 | 0 | 岗位数(自动运行) |
| StructurePoints | 1500 | 1500 | 建筑血量 |
| ConstructionWorkerCapacity | 6 | 6 | 建造工人数 |
| bWorkplace | False | False | 非工作场所 |

---

## 库房 Warehouse (Llama of Wall Street DLC)
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| CriminalInterest | 30 | 30 | 犯罪兴趣度 |
| BuildingHasBudget | False | False | 无预算 |
| BuildingHasEfficiency | False | False | 无效率 |
| BuildingHasStatistics | False | False | 无统计 |
| DefaultStorageCapacity | 10000 | **2000000** | 库存容量(200万) |
| JobCapacity | 0 | 0 | 岗位数 |
| UpkeepBase | 40 | 40 | 维护费 |
| StructurePoints | 2500 | 2500 | 建筑血量 |

---

## 电站 PowerPlant
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| ElectricityCellRadius | 30 | 30 | 电网单元半径 |
| BaseElectricityGenerationPerWorker | 100 | **200** | 每工人发电量(2x) |
| JobCapacity | 6 | **18** | 岗位数(3x) |
| MonthlyWageBase | 20 | 20 | 月薪 |
| JobQualityBase | 45 | 45 | 岗位质量 |
| WorkDuration | 90 | 90 | 工作时长 |
| UpkeepBase | 100 | 100 | 维护费 |
| StructurePoints | 6600 | 6600 | 建筑血量 |

---

## 核电站 NuclearPowerPlant
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| ElectricityCellRadius | 45 | 45 | 电网单元半径 |
| BaseElectricityGenerationPerWorker | 500 | **1000** | 每工人发电量(2x) |
| JobCapacity | 4 | **12** | 岗位数(3x) |
| MonthlyWageBase | 45 | 45 | 月薪 |
| JobQualityBase | 65 | 65 | 岗位质量 |
| WorkDuration | 80 | 80 | 工作时长 |
| UpkeepBase | 360 | 360 | 维护费 |
| StructurePoints | 8000 | 8000 | 建筑血量 |

---

## 中学 Highschool
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| StudentCapacity | 8 | **24** | 学生人数(3x) |
| JobCapacity | 4 | **12** | 就业人数(3x) |
| MonthlyWageBase | 14 | 14 | 月薪 |
| JobQualityBase | 50 | 50 | 岗位质量 |
| WorkDuration | 80 | 80 | 工作时长 |
| UpkeepBase | 45 | 45 | 维护费 |
| StructurePoints | 2400 | 2400 | 建筑血量 |
| WorkerEducation | HighSchool | HighSchool | 工人教育要求 |

---

## 大学 College
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| StudentCapacity | 8 | **24** | 学生人数(3x) |
| JobCapacity | 3 | **9** | 就业人数(3x) |
| MonthlyWageBase | 20 | 20 | 月薪 |
| JobQualityBase | 70 | 70 | 岗位质量 |
| WorkDuration | 80 | 80 | 工作时长 |
| UpkeepBase | 120 | 120 | 维护费 |
| StructurePoints | 3200 | 3200 | 建筑血量 |
| WorkerEducation | College | College | 工人教育要求 |

---

## 医院 Hospital
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **8** | 就业人数(2x) |
| VisitorsPerWorker | 6 | **12** | 每工人服务人数(2x) |
| BaseServiceQuality | 80 | 80 | 基础服务质量 |
| MonthlyWageBase | 18 | 18 | 月薪 |
| JobQualityBase | 65 | 65 | 岗位质量 |
| WorkDuration | 90 | 90 | 工作时长 |
| UpkeepBase | 80 | 80 | 维护费 |
| StructurePoints | 2800 | 2800 | 建筑血量 |

---

## 货车办公室 TeamsterOffice
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 6 | **12** | 就业人数(2x) |
| MonthlyWageBase | 8 | 8 | 月薪 |
| JobQualityBase | 45 | 45 | 岗位质量 |
| WorkDuration | 120 | 120 | 工作时长 |
| UpkeepBase | 15 | 15 | 维护费 |
| StructurePoints | 1300 | 1300 | 建筑血量 |
| ConstructionWorkerCapacity | 4 | 4 | 建造工人数 |

---

## 娱乐/奢侈娱乐建筑
全部：JobCapacity 2x、VisitorsPerWorker 2x、BaseServiceQuality 100

### 赌场 Casino
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 6 | **12** | 就业人数(2x) |
| VisitorsPerWorker | 4 | **8** | 每工人服务游客数(2x) |
| BaseServiceQuality | 70 | **100** | 服务质量(最大值) |

### 夜店 NightClub
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **8** | 就业人数(2x) |
| VisitorsPerWorker | 5 | **10** | 每工人服务游客数(2x) |
| BaseServiceQuality | 65 | **100** | 服务质量(最大值) |

### 电影院 MovieTheater
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **8** | 就业人数(2x) |
| VisitorsPerWorker | 6 | **12** | 每工人服务游客数(2x) |
| BaseServiceQuality | 70 | **100** | 服务质量(最大值) |
| ConstructionWorkerCapacity | 2 | 2 | 建造工人数 |

### 高级餐厅 GourmetRestaurant
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 6 | **12** | 就业人数(2x) |
| VisitorsPerWorker | 2 | **4** | 每工人服务游客数(2x) |
| BaseServiceQuality | 80 | **100** | 服务质量(最大值) |

### 高尔夫球场 GolfCourse
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **6** | 就业人数(1.5x) |
| BaseServiceQuality | 60 | **100** | 服务质量(最大值) |

### 卡巴莱 Cabaret
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **8** | 就业人数(2x) |
| VisitorsPerWorker | 4 | **8** | 每工人服务游客数(2x) |
| BaseServiceQuality | 65 | **100** | 服务质量(最大值) |

### 体育馆 Stadium
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 12 | **24** | 就业人数(2x) |
| VisitorsPerWorker | 5 | **10** | 每工人服务游客数(2x) |
| BaseServiceQuality | 80 | **100** | 服务质量(最大值) |
| ConstructionWorkerCapacity | 6 | 6 | 建造工人数 |

### 餐厅 Restaurant
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **8** | 就业人数(2x) |
| VisitorsPerWorker | 3 | **6** | 每工人服务游客数(2x) |
| BaseServiceQuality | 65 | **100** | 服务质量(最大值) |

### 海滩度假村 BeachResort
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **8** | 就业人数(2x) |
| VisitorsPerWorker | 5 | **10** | 每工人服务游客数(2x) |
| BaseServiceQuality | 65 | **100** | 服务质量(最大值) |
| ConstructionWorkerCapacity | 2 | 2 | 建造工人数 |

### 现代艺术馆 MuseumOfModernArt
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **8** | 就业人数(2x) |
| VisitorsPerWorker | 5 | **10** | 每工人服务游客数(2x) |
| BaseServiceQuality | 70 | **100** | 服务质量(最大值) |

### 儿童博物馆 ChildhoodMuseum
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | **8** | 就业人数(2x) |
| VisitorsPerWorker | 4 | **8** | 每工人服务游客数(2x) |
| BaseServiceQuality | 60 | **100** | 服务质量(最大值) |
| ConstructionWorkerCapacity | 4 | 4 | 建造工人数 |

### 杂货店 Grocery
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| BaseServiceQuality | 45 | **100** | 服务质量(最大值) |

### 马戏团 Circus
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| BaseServiceQuality | 45 | **100** | 服务质量(最大值) |

### 剧院 Theater
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| BaseServiceQuality | 60 | **100** | 服务质量(最大值) |

### 酒馆 Tavern
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| BaseServiceQuality | 32 | **100** | 服务质量(最大值) |

---

## 住宅
全部：HouseholdCapacity 2x、QualityOfLivingBase 100

### 乡间别墅 CountryHouse
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| HouseholdCapacity | 2 | **4** | 家庭容量(2x) |
| QualityOfLivingBase | 48 | **100** | 居住质量(最大值) |

### 工棚 Bunkhouse
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| HouseholdCapacity | 6 | **12** | 家庭容量(2x) |
| QualityOfLivingBase | 32 | **100** | 居住质量(最大值) |

### 简陋住宅 Flophouse
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| HouseholdCapacity | 9 | **18** | 家庭容量(2x) |
| QualityOfLivingBase | 38 | **100** | 居住质量(最大值) |

### 廉租房 Tenement
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| HouseholdCapacity | 16 | **32** | 家庭容量(2x) |
| QualityOfLivingBase | 40 | **100** | 居住质量(最大值) |

### 公寓 Apartment
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| HouseholdCapacity | 10 | **20** | 家庭容量(2x) |
| QualityOfLivingBase | 52 | **100** | 居住质量(最大值) |

### 彩绘公寓楼 Conventillo
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| HouseholdCapacity | 20 | **40** | 家庭容量(2x) |
| QualityOfLivingBase | 36 | **100** | 居住质量(最大值) |

### 现代公寓 ModernApartment
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| HouseholdCapacity | 16 | **32** | 家庭容量(2x) |
| QualityOfLivingBase | 80 | **100** | 居住质量(最大值) |

---

## 生产建筑 (48个)
全部：库存容量 30000、就业人数 2x、生产率保持原始

### 钢厂 SteelMill
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 8 | **16** | 就业人数(2x) |
| InStocksData.Coal.Capacity | 2560 | **30000** | 煤矿库存 |
| InStocksData.Coal.ProductionRate | 1.25 | 1.25 | 煤消耗率(原始) |
| InStocksData.Iron.Capacity | 2560 | **30000** | 铁矿库存 |
| InStocksData.Iron.ProductionRate | 1.25 | 1.25 | 铁消耗率(原始) |
| OutStocksData.Steel.Capacity | 2560 | **30000** | 钢产出库存 |
| OutStocksData.Steel.ProductionRate | 1.25 | 1.25 | 钢生产率(原始) |

### 罐头厂 Cannery
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 8 | **16** | 就业人数(2x) |
| 所有 InStocksData/OutStocksData | 2000 | **30000** | 库存容量 |
| 所有 ProductionRate | — | **原始** | 生产率不变 |

### 武器工厂 WeaponsFactory
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 8 | **16** | 就业人数(2x) |
| 所有 StocksData.Capacity | 2560 | **30000** | 库存容量 |
| 所有 ProductionRate | — | **原始** | 生产率不变 |

*(其余 45 个生产建筑同理：矿场、油田、种植园、牧场、伐木场、渔人码头、养鱼场、椰子采集、巧克力厂、家具厂、珠宝厂、塑料厂、车厂、电子厂、药厂、果汁厂、服装厂、雪茄厂、奶油厂、纺织厂、造船厂、电池厂、无人机厂、合成食物实验室、垂直农场、玩具工坊、智能家具、烟花厂、气球厂、解药炮、面具厂、自动化矿场、工业化牧场、水培种植园等)*

---

## 世界奇观 (9个)
全部：DefaultAmountBuildable 改为 OneOrMore，可无限建造

| 奇观 | 原限制 | MOD | 时代 |
|------|------|------|------|
| 布兰登堡门 BrandenburgGate | Disabled | **OneOrMore** | 殖民 |
| 圣索菲亚 HagiaSophia | Disabled | **OneOrMore** | 殖民 |
| 罗马竞技场 Colosseum | Disabled | **OneOrMore** | 冷战 |
| 狮身人面像 GreatSphinx | Disabled | **OneOrMore** | 冷战 |
| 自由女神像 StatueOfLiberty | Disabled | **OneOrMore** | 冷战 |
| 复活节岛石像 MoaiHeads | Disabled | **OneOrMore** | 二战 |
| 泰姬陵 TajMahal | Disabled | **OneOrMore** | 二战 |
| 艾菲尔铁塔 EiffelTower | Disabled | **OneOrMore** | 二战 |
| 冬宫 WinterPalace | Disabled | **OneOrMore** | 现代 |
