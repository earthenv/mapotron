from collections import OrderedDict

# Texture Measures_Display
#

CACHE_KEY = '040720151743'

palette = ','.join(['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718',
               '74A901', '66A000', '529400', '3E8601', '207401', '056201',
               '004C00', '023B01', '012E01', '011D01', '011301'])

layers = OrderedDict()
#1km data layers
layers["cv1km"] = {"asset_id":'GME/images/04040405428907908306-11218518663853966544'}
layers["range1km"] = {"asset_id":'GME/images/04040405428907908306-05815477923836018031'}
layers["std1km"] = {"asset_id":'GME/images/04040405428907908306-02047028082419114444'}
layers["CON1km"] = {"asset_id":'GME/images/04040405428907908306-05882857775063805172'}
layers["COR1km"] = {"asset_id":'GME/images/04040405428907908306-04364588802120495234'}
layers["DIS1km"] = {"asset_id":'GME/images/04040405428907908306-07066198378270623594'}
layers["ENT1km"] = {"asset_id":'GME/images/04040405428907908306-01213133461307720235'}
layers["MAX1km"] = {"asset_id":'GME/images/04040405428907908306-05737360743206721397'}
layers["VAR1km"] = {"asset_id":'GME/images/04040405428907908306-02605227334475367745'}
layers["HOM1km"] = {"asset_id":'GME/images/04040405428907908306-05646909666567200579'}
layers["mean1km"] = {"asset_id":'GME/images/04040405428907908306-11744791087859891609'}
layers["ASM1km"] = {"asset_id":'GME/images/04040405428907908306-14843257515904131603'}
layers["simpson1km"] = {"asset_id":'GME/images/04040405428907908306-02220873152218370525'}
layers["shannon1km"] = {"asset_id":'GME/images/04040405428907908306-07689614792415573083'}
layers["pielou1km"] = {"asset_id":'GME/images/04040405428907908306-14066135579949655249'}

#5km data layers
layers["cv5km"] = {"asset_id":'GME/images/04040405428907908306-09265507988909102604'}
layers["range5km"] = {"asset_id":'GME/images/04040405428907908306-09037970925087462183'}
layers["std5km"] = {"asset_id":'GME/images/04040405428907908306-17897185535166337664'}
layers["ASM5km"] = {"asset_id":'GME/images/04040405428907908306-16007788469915066807'}
layers["CON5km"] = {"asset_id":'GME/images/04040405428907908306-08787873854122892740'}
layers["COR5km"] = {"asset_id":'GME/images/04040405428907908306-16935529683843674464'}
layers["DIS5km"] = {"asset_id":'GME/images/04040405428907908306-02729983135231338734'}
layers["ENT5km"] = {"asset_id":'GME/images/04040405428907908306-13838481090293386592'}
layers["MAX5km"] = {"asset_id":'GME/images/04040405428907908306-01161003355511608542'}
layers["VAR5km"] = {"asset_id":'GME/images/04040405428907908306-03779983600507978188'}
layers["HOM5km"] = {"asset_id":'GME/images/04040405428907908306-02491034096435044717'}
layers["mean5km"] = {"asset_id":'GME/images/04040405428907908306-18008333611379033113'}
layers["pielou5km"] = {"asset_id":'GME/images/04040405428907908306-16349568220732882409'}
layers["shannon5km"] = {"asset_id":'GME/images/04040405428907908306-10124333641915897652'}
layers["simpson5km"] = {"asset_id":'GME/images/04040405428907908306-01052385432676956035'}

#25km data layers
layers["std25km"] = {"asset_id":'GME/images/04040405428907908306-02550396997934453773'}
layers["cv25km"] = {"asset_id":'GME/images/04040405428907908306-13655608845307551796'}
layers["range25km"] = {"asset_id":'GME/images/04040405428907908306-02469713014012355417'}
layers["ASM25km"] = {"asset_id":'GME/images/04040405428907908306-02125384031857337210'}
layers["CON25km"] = {"asset_id":'GME/images/04040405428907908306-00390641099377093669'}
layers["COR25km"] = {"asset_id":'GME/images/04040405428907908306-17862266891066962660'}
layers["DIS25km"] = {"asset_id":'GME/images/04040405428907908306-17462490636043232641'}
layers["ENT25km"] = {"asset_id":'GME/images/04040405428907908306-13487318828090526397'}
layers["MAX25km"] = {"asset_id":'GME/images/04040405428907908306-05120666341002128158'}
layers["VAR25km"] = {"asset_id":'GME/images/04040405428907908306-11947561923825893384'}
layers["HOM25km"] = {"asset_id":'GME/images/04040405428907908306-02379294245284288750'}
layers["mean25km"] = {"asset_id":'GME/images/04040405428907908306-15855022389511526726'}
layers["pielou25km"] = {"asset_id":'GME/images/04040405428907908306-06343935911223375604'}
layers["shannon25km"] = {"asset_id":'GME/images/04040405428907908306-02942623582260764286'}
layers["simpson25km"] = {"asset_id":'GME/images/04040405428907908306-17993289359433180784'}


palette = ','.join(['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718',
               '74A901', '66A000', '529400', '3E8601', '207401', '056201',
               '004C00', '023B01', '012E01', '011D01', '011301'])


# mapping
layers["mean25km"]["viz_params"]={"min": 0, "max": 7000,"palette":palette,"title": 'Mean_25km'}
layers["VAR25km"]["viz_params"]={"min": 0, "max": 1000000,"palette":palette, "title" : 'Variance_25km'}
layers["ASM25km"]["viz_params"]={"min": 0, "max": 4000,"palette":palette, "title" : 'Uniformity_25km'}
layers["MAX25km"]["viz_params"]={"min": 0, "max": 5000,"palette":palette, "title" : 'Maximum_25km'}
layers["HOM25km"]["viz_params"]={"min": 1500, "max": 10000,"palette":palette, "title" : 'Homogeneity_25km'}
layers["ENT25km"]["viz_params"]={"min": 0, "max": 80000,"palette":palette, "title" : 'Entropy_25km'}
layers["DIS25km"]["viz_params"]={"min": 0, "max": 50000,"palette":palette, "title" : 'Dissimilarity_25km'}
layers["COR25km"]["viz_params"]={"min": 3000, "max": 10000,"palette":palette, "title" : 'Correlation_25km'}
layers["CON25km"]["viz_params"]={"min": 0, "max": 300000,"palette":palette, "title" : 'Contrast_25km'}
layers["std25km"]["viz_params"]={"min": 0, "max": 800,"palette":palette, "title" : 'Standard deviation_25km'}
layers["simpson25km"]["viz_params"]={"min": 0, "max": 12000,"palette":palette, "title" : 'Simpson_25km'}
layers["shannon25km"]["viz_params"]={"min": 0, "max": 40000,"palette":palette, "title" : 'Shannon_25km'}
layers["range25km"]["viz_params"]={"min": 0, "max": 7000,"palette":palette, "title" : 'Range_25km'}
layers["pielou25km"]["viz_params"]={"min": 0, "max": 10000,"palette":palette, "title" : 'Pielou_25km'}
layers["cv25km"]["viz_params"]={"min": 0, "max": 5000, "palette":palette, "title" : 'Coefficient of Variation_25km'}


layers["mean5km"]["viz_params"]={"min": 0, "max": 8000,"palette":palette, "title" : 'Mean_5km'}
layers["VAR5km"]["viz_params"]={"min": 0, "max": 1000000,"palette":palette, "title" : 'Variance_5km'}
layers["ASM5km"]["viz_params"]={"min": 0, "max": 5000,"palette":palette, "title" : 'Uniformity_5km'}
layers["MAX5km"]["viz_params"]={"min": 0, "max": 8000,"palette":palette, "title" : 'Maximum_5km'}
layers["HOM5km"]["viz_params"]={"min": 1500, "max": 10000,"palette":palette, "title" : 'Homogeneity_5km'}
layers["ENT5km"]["viz_params"]={"min": 0, "max": 70000,"palette":palette, "title" : 'Entropy_5km'}
layers["DIS5km"]["viz_params"]={"min": 0, "max": 70000,"palette":palette, "title" : 'Dissimilarity_5km'}
layers["COR5km"]["viz_params"]={"min": 4000, "max": 10000,"palette":palette, "title" : 'Correlation_5km'}
layers["CON5km"]["viz_params"]={"min": 0, "max": 500000,"palette":palette, "title" : 'Contrast_5km'}
layers["std5km"]["viz_params"]={"min": 0, "max": 1500,"palette":palette, "title" : 'Standard deviation_5km'}
layers["simpson5km"]["viz_params"]={"min": 1000, "max": 12000, "palette":palette, "title" : 'Simpson_5km'}
layers["shannon5km"]["viz_params"]={"min": 0, "max": 35000, "palette":palette, "title" : 'Shannon_5km'}
layers["range5km"]["viz_params"]={"min": 0, "max": 7000,"palette":palette, "title" : 'Range_5km'}
layers["pielou5km"]["viz_params"]={"min": 5000, "max": 10000, "palette":palette, "title" : 'Pielou_5km'}
layers["cv5km"]["viz_params"]={"min": 0, "max": 5000, "palette":palette, "title" : 'Coefficient of variation_5km'}

layers["mean1km"]["viz_params"]={"min": 0, "max": 8000,"palette":palette, "title" : 'Mean_1km'}
layers["VAR1km"]["viz_params"]={"min": 0, "max": 300000,"palette":palette, "title" : 'Variance_1km'}
layers["ASM1km"]["viz_params"]={"min": 300, "max": 10000,"palette":palette, "title" : 'Uniformity_1km'}
layers["MAX1km"]["viz_params"]={"min": 0, "max": 8000,"palette":palette, "title" : 'Maximum_1km'}
layers["HOM1km"]["viz_params"]={"min": 0, "max": 10000,"palette":palette, "title" : 'Homogeneity_1km'}
layers["ENT1km"]["viz_params"]={"min": 0, "max": 38000,"palette":palette, "title" : 'Entropy_1km'}
layers["DIS1km"]["viz_params"]={"min": 0, "max": 70000,"palette":palette, "title" : 'Dissimilarity_1km'}
layers["COR1km"]["viz_params"]={"min": 0, "max": 7000,"palette":palette, "title" : 'Correlation_1km'}
layers["CON1km"]["viz_params"]={"min": 0, "max": 400000,"palette":palette, "title" : 'Contrast_1km'}
layers["std1km"]["viz_params"]={"min": 0, "max": 800,"palette":palette, "title" : 'Standard deviation_1km'}
layers["simpson1km"]["viz_params"]={"min": 3000, "max": 10000,"palette":palette, "title" : 'Simpson_1km'}
layers["shannon1km"]["viz_params"]={"min": 0, "max": 27000,"palette":palette, "title" : 'Shannon_1km'}
layers["pielou1km"]["viz_params"]={"min": 5000, "max": 10000,"palette":palette, "title" : 'Pielou_1km'}
layers["range1km"]["viz_params"]={"min": 0, "max": 3000,"palette":palette, "title" : 'Range_1km'}
layers["cv1km"]["viz_params"]={"min": 0, "max": 2000, "palette":palette, "title" : 'Coefficient of Variation_1km'}
