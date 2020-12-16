import json
import requests
import ee

config = json.loads(requests.get(
    'http://earthenv.org/map_config/config.json').content)

collections = {}
for collection in config:
    collections[collection["id"]] = {
        "title": collection["title"], "layers": {}}
    for feature in collection["features"]:
        collections[collection["id"]]["layers"][feature["layer_id"]] = feature

ee.Initialize()

# import ee

# GEE_SERVICE_ACCOUNT = "ACC"
# GEE_SERVICE_KEY = "PATH"

# EE_CREDENTIALS = ee.ServiceAccountCredentials(GEE_SERVICE_ACCOUNT, GEE_SERVICE_KEY)

# ee.Initialize(credentials=EE_CREDENTIALS)
