import json
import os
import cache
from google.appengine.api import urlfetch

config = json.loads(urlfetch.fetch(
    url='https://earthenv.org/map_config/config.json',
    method=urlfetch.GET,
    deadline=600).content)

collections = {}
for collection in config:
    collections[collection["id"]]={"title":collection["title"],"layers":{}}
    for feature in collection["features"]:
        collections[collection["id"]]["layers"][feature["layer_id"]]=feature

cache.add('mapotron-maps',json.dumps(collections))
