import json
import requests
import ee

# config = json.loads(requests.get(
#     'http://earthenv.org/map_config/config.json').content)

# Use local config.json
with open('static/config.json') as cf:
    config = json.load(cf)

collections = {}
for collection in config:
    collections[collection["id"]] = {
        "title": collection["title"], "layers": {}}
    for feature in collection["features"]:
        collections[collection["id"]]["layers"][feature["layer_id"]] = feature

# ee.Initialize()

GEE_SERVICE_ACCOUNT = "map-of-life@appspot.gserviceaccount.com"
GEE_SERVICE_KEY = "keys/map-of-life-6095c82f9146.json"

EE_CREDENTIALS = ee.ServiceAccountCredentials(GEE_SERVICE_ACCOUNT, GEE_SERVICE_KEY)

ee.Initialize(credentials=EE_CREDENTIALS)
