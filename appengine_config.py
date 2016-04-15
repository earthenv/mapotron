import json
import os
import cache
from google.appengine.api import urlfetch

config = json.loads(urlfetch.fetch(
    url='http://path/to/map/config.json',
    method=urlfetch.GET,
    deadline=600).content)

collections = {}
for collection in config:
    collections[collection["id"]]={"title":collection["title"],"layers":{}}
    for feature in collection["features"]:
        collections[collection["id"]]["layers"][feature["layer_id"]]=feature

cache.add('earthenv-maps',json.dumps(collections))
