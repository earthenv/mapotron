"""
   Wraps the EE Image.getMapId method to allow map tiles to be regenerated 
   given key, zoom, x, and y tile parameters.
"""

__author__ = "Jeremy Malczyk"

import logging
import cache
import json
import ee

EE_TILE_URL = 'https://earthengine.googleapis.com/map/%s/{Z}/{X}/{Y}?token=%s'

# Wraps ee.Image.getMapId() to log mapid/token and serialized ee request
#
def getMap(image, viz_params, key):
    #get map obj
    ee_map = image.getMapId(viz_params)

    map_key = 'cloudmapcache_%s' % key

    cache.add(map_key, json.dumps({
        "mapid": ee_map["mapid"],
        "token": ee_map["token"]
    }))

    #store the ee request that goes with it
    ee_key = 'eecache_%s' % (key)

    cache.add(ee_key, json.dumps({
        "mapid": ee_map["mapid"],
        "viz_params": viz_params,
        "image": ee.serializer.encode(ee_map["image"])
    }))

    return ee_map
