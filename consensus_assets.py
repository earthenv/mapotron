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

palette = ','.join(['FFFFFF', 'CE7E45', 'DF923D', 'F1B555', 'FCD163', '99B718',
               '74A901', '66A000', '529400', '3E8601', '207401', '056201',
               '004C00', '023B01', '012E01', '011D01', '011301'])



# Monthly Layers
layers = OrderedDict()
layers["evergreen_deciduous_needleleaf_trees"]= {
    "title" : "Evergreen/Deciduous Needleleaf Trees",
	"asset_id" : "GME/images/04040405428907908306-11593846612392477969",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["evergreen_broadleaf_trees"] = {
    "title" : "Evergreen Broadleaf Trees",
	"asset_id" : "GME/images/04040405428907908306-13229186913119943316",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["deciduous_broadleaf_trees"] = {
    "title" : "Deciduous Broadleaf Trees",
	"asset_id" : "GME/images/04040405428907908306-16121583928322922417",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["mixed_other_trees"] = {
    "title" : "Mixed/Other Trees",
	"asset_id" : "GME/images/04040405428907908306-17238109668775876592",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["shrubs"] = {
    "title" : "Shrubs",
	"asset_id" : "GME/images/04040405428907908306-06541804430193116641",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["herbaceous_vegetation"] = {
    "title" : "Herbaceous Vegetation",
	"asset_id" : "GME/images/04040405428907908306-06125469435409697790",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["cultivated_and_managed_vegetation"] = {
    "title" : "Cultivated and Managed Vegetation",
	"asset_id" : "GME/images/04040405428907908306-10318607417242881135",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["regularly_flooded_vegetation"] = {
    "title" : "Regularly Flooded Vegetation",
	"asset_id" : "GME/images/04040405428907908306-10758914561056934058",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["Urban_built_up"] = {
    "title" : "Urban/Built-up",
	"asset_id" : "GME/images/04040405428907908306-16854579656863010645",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["snow_ice"] = {
    "title" : "Snow/Ice",
	"asset_id" : "GME/images/04040405428907908306-14572693522792218524",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["barren"] = {
    "title" : "Barren",
	"asset_id" : "GME/images/04040405428907908306-15250273117323094408",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["open_water"] = {
    "title" : "Open Water",
	"asset_id" : "GME/images/04040405428907908306-09426288588791571721",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
layers["shrubs"] = {
    "title" : "Shrubs",
	"asset_id" : "GME/images/04040405428907908306-06541804430193116641",
	"viz_params" : {
		"min": 1,"max": 100, "palette":palette, "opacity":0.6
    }
}
