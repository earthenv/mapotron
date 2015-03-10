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
	spatial = "ffffff,0000ff,00ff00,ff0000,ff0000")

# Monthly Layers
layers = OrderedDict(
    Layer_One= {
        "title" : "The first layer",
    	"asset_id" : "GME/images/some-imageid",
    	"viz_params" : {
    		"min": 0, "max": 2000,
    		"palette": PALETTES["spatial"]
        }
    },
    Another_Layer = {
        "title" : "Another layer...",
    	"asset_id" : "GME/images/another-imageid",
    	"viz_params" : {
    		"min": 0, "max": 1500,
    		"palette" : PALETTES["bgr"]
        }
    },
    You_get_the_point = {
        "title" : "You get the point",
    	"asset_id" : "GME/images/yetonemore-imageid",
    	"viz_params" : {
    		"min": 0, "max": 2500,
    		"palette": PALETTES["blue"]
        }
    }
)
