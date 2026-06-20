# MyMod 模组内容

## 警卫塔 ColonialGuardTower
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| DamagePerWorker.RangeMin | 1.4 | 500 | 最低攻击力 |
| DamagePerWorker.RangeMax | 2.6 | 500 | 最高攻击力 |
| AggroRange | 10 | 30 | 警戒范围(3x) |
| GeneratorRadius (MilitaryStrength) | 10 | 30 | 军事力量覆盖半径 |

## 警察局 PoliceStation
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| GeneratorRadius | 20 | 99999 | 安保覆盖半径，全图 |
| GeneratorInfluence | 45 | 100 | 安保强度(安全度) |
| GeneratorIntensityDropOffset | Drop0 | Drop0 | 覆盖边缘不衰减 |

## 监狱 Prison
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| DetentionSlots | 32 | 255 | 罪犯容量上限 |

## 电视台 TVStation
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| GeneratorRadius | 60 | 999999 | 自由覆盖半径，全图 |
| InfluenceRange | 60 | 999999 | 影响范围 |
| 第一频道 LibertyGeneratorDelta | -30 | 100 | 全图自由度+100 |

## 大型广场 2x2 Square
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| GeneratorRadius | 5 | 99999 | 美观覆盖半径，全图 |
| GeneratorInfluence | 14 | 100 | 美观度强度 |

## 垃圾填埋厂 GarbageDump
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| CleansingRadius | 30 | 99999 | 净化半径，全图 |
| AbsolutePollutionDecrease | 0.01 | 100 | 污染降低值 |
| bGeneratePollutionIfNotOperational | True | False | 不工作时不再产生污染 |

## 变电站 ElectricSubstation
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| InfluenceRange | 60 | 99999999 | 供电覆盖范围，全图 |

## 地铁站 MetroStation
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| InfluenceRange | 10 | 999999 | 通勤覆盖范围，全图 |
| JobCapacity | 2 | 6 | 岗位数(3x) |

## 回收装置 Reclaimer (DLC)
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| InfluenceRange | 7.5 | 999999 | 回收覆盖范围，全图 |
| DefaultMaximumCapacityOfOutStock | 2000 | 30000 | 最大产出库存 |

## 库房 Warehouse (DLC)
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| DefaultStorageCapacity | 10000 | 2000000 | 库存容量(200万) |

## 电站 PowerPlant
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| BaseElectricityGenerationPerWorker | 100 | 200 | 发电量(2x) |
| JobCapacity | 6 | 18 | 就业人数(3x) |

## 核电站 NuclearPowerPlant
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| BaseElectricityGenerationPerWorker | 500 | 1000 | 发电量(2x) |
| JobCapacity | 4 | 12 | 就业人数(3x) |

## 中学 Highschool
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| StudentCapacity | 8 | 24 | 学生人数(3x) |
| JobCapacity | 4 | 12 | 就业人数(3x) |

## 大学 College
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| StudentCapacity | 8 | 24 | 学生人数(3x) |
| JobCapacity | 3 | 9 | 就业人数(3x) |

## 医院 Hospital
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 4 | 8 | 就业人数(2x) |
| VisitorsPerWorker | 6 | 12 | 服务人数(2x) |

## 货车办公室 TeamsterOffice
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| JobCapacity | 6 | 12 | 就业人数(2x) |

## 娱乐/奢侈娱乐建筑
所有娱乐建筑：JobCapacity 2x、VisitorsPerWorker 2x、BaseServiceQuality 100

| 建筑 | JobCapacity | VisitorsPerWorker | ServiceQuality |
|------|------|------|------|
| 赌场 Casino | 6→12 | 4→8 | 70→100 |
| 夜店 NightClub | 4→8 | 5→10 | 65→100 |
| 电影院 MovieTheater | 4→8 | 6→12 | 70→100 |
| 高级餐厅 GourmetRestaurant | 6→12 | 2→4 | 80→100 |
| 高尔夫 GolfCourse | 4→6 | — | 60→100 |
| 卡巴莱 Cabaret | 4→8 | 4→8 | 65→100 |
| 体育馆 Stadium | 12→24 | 5→10 | 80→100 |
| 餐厅 Restaurant | 4→8 | 3→6 | 65→100 |
| 海滩度假村 BeachResort | 4→8 | 5→10 | 65→100 |
| 现代艺术馆 Museum | 4→8 | 5→10 | 70→100 |
| 儿童博物馆 ChildhoodMuseum | 4→8 | 4→8 | 60→100 |
| 杂货店 Grocery | — | — | 45→100 |
| 马戏团 Circus | — | — | 45→100 |
| 剧院 Theater | — | — | 60→100 |
| 酒馆 Tavern | — | — | 32→100 |

## 住宅 (7种)
| 建筑 | HouseholdCapacity | QualityOfLivingBase |
|------|------|------|
| 乡间别墅 CountryHouse | 2→4 | 48→100 |
| 工棚 Bunkhouse | 6→12 | 32→100 |
| 简陋住宅 Flophouse | 9→18 | 38→100 |
| 廉租房 Tenement | 16→32 | 40→100 |
| 公寓 Apartment | 10→20 | 52→100 |
| 彩绘公寓楼 Conventillo | 20→40 | 36→100 |
| 现代公寓 ModernApartment | 16→32 | 80→100 |

## 生产建筑 (48个工厂/矿场/农场等)
| 属性 | 原值 | MOD值 | 说明 |
|------|------|------|------|
| InStocksData / OutStocksData Capacity | 2000~5000 | 30000 | 库存容量 |
| ProductionRate | — | 原始不变 | 生产率 |
| JobCapacity | — | 2x | 就业人数 |

## 世界奇观 (9个)
所有奇观的 DefaultAmountBuildable 改为 OneOrMore，不再限制只能建1个：
布兰登堡门、圣索菲亚、罗马竞技场、狮身人面像、自由女神像、复活节岛石像、泰姬陵、艾菲尔铁塔、冬宫
