#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


import webapp2
import logging
import cache
import json
import config_creds
import ee_assets
import ee
import config
import services


from google.appengine.api import images


from google.appengine.api import urlfetch

EE_TILE_URL = 'https://earthengine.googleapis.com/map/%s/%i/%i/%i?token=%s'




class QueryHandler(webapp2.RequestHandler):
    def sample(self, collection, x, y):

        x=float(x)
        y=float(y)

        key = "earthenv-maps-query-3-%s-%s-%s" % (collection, x,y)
        response = services.checkCache(key)
        if response is None:
            images = []

            for k,v in ee_assets.layers[collection]["layers"].items():
                logging.info(v)
                if "query_assets" in v:
                    for a in v["query_assets"]:
                        images.append(ee.Image(a["id"]).set(a).set(
                            "name",k).set("image", a["name"]))

                else:
                    images.append(ee.Image(v["id"]).set(v).set(
                        "name",k).set("image",k))

            result = ee.ImageCollection(images).map(
                lambda i:
                    ee.Feature(None).copyProperties(i).set(
                        "values", i.reduceRegion(
                            reducer=ee.Reducer.first(),
                            geometry=ee.Geometry.Point([x,y])))
                ).getInfo()

            logging.info(result)
            response = {}
            for feature in result["features"]:
                print(feature)
                try:
                    if feature["properties"]["name"] not in response:
                        response[feature["properties"]["name"]] = []
                    response[feature["properties"]["name"]].append(feature["properties"])
                except Exception as e:
                    logging.info(e)
                    #response[feature["properties"]["name"]] = None

        services.writeResult(response,self.response)


application = webapp2.WSGIApplication([
    webapp2.Route(r'/api/query/sample/<collection>/<x>/<y>',
        handler='query_handler.QueryHandler:sample')],
    debug=True)
