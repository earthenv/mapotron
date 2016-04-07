from collections import OrderedDict

# Texture Measures_Display
#

palette = ','.join(['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718',
               '74A901', '66A000', '529400', '3E8601', '207401', '056201',
               '004C00', '023B01', '012E01', '011D01', '011301'])

# 1km data layers
layers = OrderedDict()
layers["cv1km"] = {"asset_id" :"GME/images/04040405428907908306-08769780043203035842"}
layers["range1km"] = {"asset_id" :'GME/images/04040405428907908306-10394247160207865085'}
layers["skew1km"] = {"asset_id" :'GME/images/04040405428907908306-07105617679542874626'}
layers["std1km"] = {"asset_id" :'GME/images/04040405428907908306-13158260552952326856'}
layers["ASM1km"] = {"asset_id" :'GME/images/04040405428907908306-16406670214051324443'}
layers["CON1km"] = {"asset_id" :'GME/images/04040405428907908306-06218832765351601826'}
layers["COR1km"] = {"asset_id" :'GME/images/04040405428907908306-14384248069043557070'}
layers["DIS1km"] = {"asset_id" :'GME/images/04040405428907908306-00340166808767427321'}
layers["ENT1km"] = {"asset_id" :'GME/images/04040405428907908306-11571836497751865875'}
layers["MAX1km"] = {"asset_id" :'GME/images/04040405428907908306-17186655785509932638'}
layers["VAR1km"] = {"asset_id" :'GME/images/04040405428907908306-18246010244860203985'}
layers["HOM1km"] = {"asset_id" :'GME/images/04040405428907908306-00435933812149385860'}
layers["mean1km"] = {"asset_id" :'GME/images/04040405428907908306-03420776235432736632'}

# 5km data layers
layers["cv5km"] = {"asset_id" :'GME/images/04040405428907908306-17542476903778658556'}
layers["range5km"] = {"asset_id" :'GME/images/04040405428907908306-13491703285284086142'}
layers["skew5km"] = {"asset_id" : 'GME/images/04040405428907908306-13986410341003586656'}
layers["std5km"] = {"asset_id" :'GME/images/04040405428907908306-03999848393837914801'}
layers["ASM5km"] = {"asset_id" :'GME/images/04040405428907908306-09088546738262949649'}
layers["CON5km"] = {"asset_id" :'GME/images/04040405428907908306-13525483602529161990'}
layers["COR5km"] = {"asset_id" :'GME/images/04040405428907908306-04777756904744142271'}
layers["DIS5km"] = {"asset_id" :'GME/images/04040405428907908306-00350904358295040349'}
layers["ENT5km"] = {"asset_id" :'GME/images/04040405428907908306-15932048015753722196'}
layers["MAX5km"] = {"asset_id" :'GME/images/04040405428907908306-07207780322193669978'}
layers["VAR5km"] = {"asset_id" :'GME/images/04040405428907908306-09411254791553839345'}
layers["HOM5km"] = {"asset_id" :'GME/images/04040405428907908306-12895906859963011145'}
layers["mean5km"] = {"asset_id" :'GME/images/04040405428907908306-06254051819344683407'}

# 25km data layers
layers["skew25km"] = {"asset_id" :'GME/images/04040405428907908306-07087875517047517209'}
layers["std25km"] = {"asset_id" :'GME/images/04040405428907908306-05910641428878254068'}
layers["cv25km"] = {"asset_id" :'GME/images/04040405428907908306-00863338518101757657'}
layers["range25km"] = {"asset_id" :'GME/images/04040405428907908306-01513445998625551942'}
layers["ASM25km"] = {"asset_id" :'GME/images/04040405428907908306-17978804419936700633'}
layers["CON25km"] = {"asset_id" :'GME/images/04040405428907908306-02742294854070549037'}
layers["COR25km"] = {"asset_id" :'GME/images/04040405428907908306-00994941935908517353'}
layers["DIS25km"] = {"asset_id" :'GME/images/04040405428907908306-11936674333854593174'}
layers["ENT25km"] = {"asset_id" :'GME/images/04040405428907908306-09128243754984439107'}
layers["MAX25km"] = {"asset_id" :'GME/images/04040405428907908306-10038450289605903921'}
layers["VAR25km"] = {"asset_id" :'GME/images/04040405428907908306-00679710118225927594'}
layers["HOM25km"] = {"asset_id" :'GME/images/04040405428907908306-16543930984115861572'}
layers["mean25km"] = {"asset_id" :'GME/images/04040405428907908306-14022868310692561970'}


# mapping 
layers["cv25km"]["viz_params"] = {"min": 0, "max": 0.5, "palette":palette}
layers["range25km"]["viz_params"] = {"min": 0, "max": 7000,"palette":palette}
layers["skew25km"]["viz_params"] = {"min": -1, "max": 1,"palette":palette}
layers["std25km"]["viz_params"] = {"min": 0, "max": 800,"palette":palette}
layers["ASM25km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["CON25km"]["viz_params"] = {"min": 0, "max": 50,"palette":palette}
layers["COR25km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["DIS25km"]["viz_params"] = {"min": 0, "max": 5,"palette":palette}
layers["ENT25km"]["viz_params"] = {"min": 0, "max": 8,"palette":palette}
layers["HOM25km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["MAX25km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["VAR25km"]["viz_params"] = {"min": 0, "max": 100,"palette":palette}
layers["mean25km"]["viz_params"] = {"min": 0, "max": 10000,"palette":palette}
layers["cv5km"]["viz_params"] = {"min": 0, "max": 0.5, "palette":palette}
layers["range5km"]["viz_params"] = {"min": 0, "max": 7000,"palette":palette}
layers["skew5km"]["viz_params"] = {"min": -0.8, "max": 1,"palette":palette}
layers["std5km"]["viz_params"] = {"min": 0, "max": 1500,"palette":palette}
layers["ASM5km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["CON5km"]["viz_params"] = {"min": 0, "max": 50,"palette":palette}
layers["COR5km"]["viz_params"] = {"min": 0.4, "max": 1,"palette":palette}
layers["DIS5km"]["viz_params"] = {"min": 0, "max": 7,"palette":palette}
layers["ENT5km"]["viz_params"] = {"min": 0, "max": 7,"palette":palette}
layers["HOM5km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["MAX5km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["VAR5km"]["viz_params"] = {"min": 0, "max": 100,"palette":palette}
layers["mean5km"]["viz_params"] = {"min": 0, "max": 10000,"palette":palette}
layers["cv1km"]["viz_params"] = {"min": 0, "max": 0.2, "palette":palette}
layers["range1km"]["viz_params"] = {"min": 0, "max": 3000,"palette":palette}
layers["skew1km"]["viz_params"] = {"min": -0.8, "max": 1,"palette":palette}
layers["std1km"]["viz_params"] = {"min": 0, "max": 800,"palette":palette}
layers["ASM1km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["CON1km"]["viz_params"] = {"min": 0, "max": 50,"palette":palette}
layers["COR1km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["DIS1km"]["viz_params"] = {"min": 0, "max": 7,"palette":palette}
layers["ENT1km"]["viz_params"] = {"min": 0, "max": 4.5,"palette":palette}
layers["HOM1km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["MAX1km"]["viz_params"] = {"min": 0, "max": 1,"palette":palette}
layers["VAR1km"]["viz_params"] = {"min": 0, "max": 40,"palette":palette}
layers["mean1km"]["viz_params"] = {"min": 0, "max": 10000,"palette":palette}
