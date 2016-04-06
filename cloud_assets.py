from collections import OrderedDict

# Cloud Data Display
#

# Monthly Layers
layers = OrderedDict()

layers["Cloud Forest Prediction"] = {
    "index":0,"show":False,"units":"predict","legend":"Cloud_Forest_Prediction",
    "asset_id" :'users/map-of-life/CloudForestPrediction_Cloud2'}

# Derived layers
layers["Mean annual"] = {"index":1,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-16997968935033932234'}
layers["Seasonality"] = {"index":2,"show":True,"units":"seasonality","legend":"Seasonality","asset_id" :'GME/images/04040405428907908306-15930837556503781845',
    'query_assets': [
        {
            'name':'Seasonality concentration',
            'units':'sci',
            'tooltip':'Seasonal concentration index (0-100)',
            'asset_id':'users/map-of-life/environmental/MODCF_seasonality_concentration'
        },
        {
            'name':'Seasonality theta',
            'units':'theta',
            'tooltip':'Central date of season with greatest cloud concentration',
            'asset_id':'users/map-of-life/environmental/MODCF_seasonality_theta'}
    ]}
layers["Intra-annual variation (SD)"] = {"index":3,"show":False,"units":"standard-deviation","legend":"Intra-Annual_SD","asset_id" :'GME/images/04040405428907908306-07437080423447650359'}
layers["Inter-annual variation (SD)"] = {"index":4,"show":False,"units":"standard-deviation","legend":"Inter-Annual_SD","asset_id" :'GME/images/04040405428907908306-02080883188484482342'}
layers["Spatial variation (SD)"] = {"index":5,"show":False,"units":"standard-deviation","legend":"Spatial_SD_100_km","asset_id" :'GME/images/04040405428907908306-02162961494482888597'}
layers["Stability Hotspots"] = {
    "index":6,"show":False,
    "units":"hotspots",
    "legend":"Stability_Hotspots",
    "asset_id" :'GME/images/04040405428907908306-12449242623476995492',
    "querytoggle":["Intra-annual variation (SD)","Inter-annual variation (SD)"]}

# Monthly Layers
layers["January"] = {"index":7,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :"GME/images/04040405428907908306-03704860762625123026"}
layers["February"] = {"index":8,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-08263346736151798208'}
layers["March"] = {"index":9,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-02975791319561448122'}
layers["April"] = {"index":10,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-16223682928559322200'}
layers["May"] = {"index":11,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-08342255940990292930'}
layers["June"] = {"index":12,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-05993230520086579332'}
layers["July"] = {"index":13,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-09155748088421148850'}
layers["August"] = {"index":14,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-09109707975859833322'}
layers["September"] = {"index":15,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-09109707975859833322'}
layers["October"] = {"index":16,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-16061826233786718607'}
layers["November"] = {"index":17,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-06187712058419700440'}
layers["December"] = {"index":18,"show":False,"units":"percentage","legend":"cloud_frequency","asset_id" :'GME/images/04040405428907908306-08119494764782299088'}

# define palettes
palette_blues="08306b,0d57a1,2878b8,4997c9,72b2d7,a2cbe2,c7dcef,deebf7,f7fbff"
palette_bgr="0000ff,00ff00,ff0000"
palette_spatial="ffffff,0000ff,00ff00,ff0000,ff0000"

## Define the viz_params
for layer in ("Mean annual","January","February","March","April","May","June","July","August","September","October","November","December"):
 layers[layer]["viz_params"] = {"min": 0, "max": 10000, "palette":palette_blues}

layers["Spatial variation (SD)"]["viz_params"] = {"min": 0, "max": 2000,"palette":palette_spatial}
layers["Cloud Forest Prediction"]["viz_params"] = {"min": 0, "max": 0.01,"palette":palette_spatial}
layers["Inter-annual variation (SD)"]["viz_params"] = {"min": 0, "max": 1500,"palette":palette_bgr}
layers["Intra-annual variation (SD)"]["viz_params"] = {"min": 0, "max": 2500,"palette":palette_bgr}

## These two are RGB images
layers["Seasonality"]["viz_params"] = {}
layers["Stability Hotspots"]["viz_params"] = {}


#crop antarctica
# Monthly Layers
#geodesic = ee.Geometry.Rectangle(-180, -60, 180, 85)
#bbox = ee.Geometry(geodesic, none, false)
