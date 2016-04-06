"""
   Configuration module for the mapotron.

   Raster assets stored on MapsEngine, or vector assets stored in Fusion Tables
   must be accessible by the application id in order to work.
   Layers will be displayed in the order defined, and titled in the UI
   using the dictionary key for the asset. Any legends should be placed in
   the /app/img/legend folder as asset-key.png
"""

__author__ = 'Jeremy Malczyk'

from collections import OrderedDict

# Some palettes

PALETTES = dict(
	blue = "08306b,0d57a1,2878b8,4997c9,72b2d7,a2cbe2,c7dcef,deebf7,f7fbff",
	bgr = "0000ff,00ff00,ff0000",
	spatial = "ffffff,0000ff,00ff00,ff0000")


palette = PALETTES["spatial"]
# Monthly Layers
layers = OrderedDict()

layers["Evergreen_deciduous_needleleaf_trees_avg"] = {
   "title" : "Evergreen deciduous needleleaf trees (avg)",
   "asset_id" : 'GME/images/04040405428907908306-18223818104584807358',
   "viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Evergreen_broadleaf_trees_avg"] = {
   "title" : "Evergreen broadleaf trees (avg)",
   "asset_id" : 'GME/images/04040405428907908306-06288355460665902052',
   "viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Deciduous_broadleaf_trees_avg"] = {
"title" : "Deciduous broadleaf trees (avg)",
"asset_id" : 'GME/images/04040405428907908306-06328252012425307056',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Mixed_other_trees_avg"] = {
"title": "Mixed other trees (avg)",
"asset_id" : 'GME/images/04040405428907908306-06815775574853865980',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Shrubs_avg"] = {
"title": "Shrubs (avg)",
"asset_id" : 'GME/images/04040405428907908306-00203113007363780479',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Herbaceous_vegetation_avg"] = {
"title": "Herbaceous vegetation (avg)",
"asset_id" : 'GME/images/04040405428907908306-16835818123240771741',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Cultivated_and_managed_vegetation_avg"] = {
"title": "Cultivated and managed vegetation (avg)",
"asset_id" : 'GME/images/04040405428907908306-08243630565672835151',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Regularly_flooded_shrub_herbaceous_vegetation_avg"] = {
"title": "Regularly flooded shrub herbaceous vegetation (avg)",
"asset_id" : 'GME/images/04040405428907908306-03244650415831943436',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Urban_builtup_avg"] = {
"title":"Urban builtup (avg)",
"asset_id" : 'GME/images/04040405428907908306-15614867271382850622',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Snow_ice_avg"] = {
"title": "Snow/ice (avg)",
"asset_id" : 'GME/images/04040405428907908306-06438909179914905042',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Barren_lands_sparse_vegetation_avg"] = {
"title": "Barren lands sparse vegetation (avg)",
"asset_id" : 'GME/images/04040405428907908306-00046983562667843989',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Open_water_avg"] = {
"title": "Open water (avg)",
"asset_id" : 'GME/images/04040405428907908306-17335493681532941844',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Mean_annual_air_temperature_avg"] = {
"title": "Mean annual air temperature (avg)",
"asset_id" : 'GME/images/04040405428907908306-14021161906445875414',
"viz_params" : {"min":0,"max":300,"palette":palette}
}
layers["Annual_air_temperature_range_avg"] = {
"title": "Annual air temperature range (avg)",
"asset_id" : 'GME/images/04040405428907908306-17420260840459206438',
"viz_params" : {"min":76,"max":500,"palette":palette}
}
layers["Annual_sum_of_precipitation_avg"] = {
"title": "Annual sum of precipitation (avg)",
"asset_id" : 'GME/images/04040405428907908306-03748644437782705176',
"viz_params" : {"min":0,"max":20000000,"palette":palette}
}
layers["Precipitation_seasonality_avg"] = {
"title" : "Precipitation seasonality (avg)",
"asset_id" : 'GME/images/04040405428907908306-05408005842133179591',
"viz_params" : {"min":0,"max":100,"palette":palette}
}
layers["Catchment_size_sum"] = {
"title":"Catchment size (sum)",
"asset_id" : 'GME/images/04040405428907908306-14916877419814061790',
"viz_params" : {"min":1,"max":5000,"palette":palette}
}
layers["Stream_length_sum"] = {
"title": "Stream length (sum)",
"asset_id" :  'GME/images/04040405428907908306-18258810609658841024',
"viz_params" : {"min":1,"max":500,"palette":palette}
}
layers["Elevation_avg"] = {
"title": "Elevation (avg)",
"asset_id" :  'GME/images/04040405428907908306-14725983039031760735',
"viz_params" : {"min":0,"max":3000,"palette":palette}
}
layers["Elevation_range"] = {
"title": "Elevation range",
"asset_id" :  'GME/images/04040405428907908306-01331975681272697730',
"viz_params" : {"min":0,"max":3000,"palette":palette}
}
layers["Slope_avg"] = {
"title": "Slope (avg)",
"asset_id" :  'GME/images/04040405428907908306-15738620217066490177',
"viz_params" : {"min":0,"max":500,"palette":palette}
}
layers["Slope_range"] = {
"title" : "Slope range",
"asset_id" :  'GME/images/04040405428907908306-18241744787223608951',
"viz_params" : {"min":0,"max":500,"palette":palette}
}
layers["Precambrian_surface_lithology_wsum"] = {
"title" : "Precambrian surface lithology (wsum)",
"asset_id" :  'GME/images/04040405428907908306-17269292502416777314',
"viz_params" : {"min":0,"max":40,"palette":palette}
}
layers["Quaternary_surface_lithology_wsum"] = {
"title" : "Quaternary surface lithology (wsum)",
"asset_id" :  'GME/images/04040405428907908306-17590838206930784687',
"viz_params" : {"min":0,"max":40,"palette":palette}
}
