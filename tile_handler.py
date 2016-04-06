#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import services
import webapp2
import logging
import cache
import json
import config_creds
import ee_assets


from google.appengine.api import images


from google.appengine.api import urlfetch

EE_TILE_URL = 'https://earthengine.googleapis.com/map/%s/%i/%i/%i?token=%s'




class TileHandler(webapp2.RequestHandler):
    def checkCoords(self, z,x,y):
        if y<0 or y>=2**z:
            return False
        else:
            return True

    def get(self, key, z, x, y):
        z=int(z)
        x=int(x)
        y=int(y)
        #check tile coords
        if self.checkCoords(z,x,y):
            while x < 0:
                x = x + 2**z
            while x >= 2**z:
                x = x- 2**z
            self.getTile(key,z,x,y)
        else:
            logging.info('Coords out of range, serving blank.')
            tile = open('empty.png', 'r').read()
            services.writeResult(tile, self.response, format='image/png')

    def getTile(self,key,z,x,y):

        #first try and fetch from cache
        tile_key = 'cloudtilecache5_%s_%i_%i_%i' % (key, int(z), int(x), int(y))
        tile = services.checkCache(tile_key, type='blob')



        try:
            #test tile image
            image = images.Image(image_data=tile)
            logging.info("Image format %s" % image.format)
            if image.format >= 0:
                logging.info('serving image from cache')
                services.writeResult(tile, self.response, format = 'image/png')
            else:
                raise Exception('format','Bad format in blobstore')
        except Exception as e:
            logging.info(e)
            #No tile available, find the latest mapid/token for this key
            map_key =  'cloudmapcache5_%s' % (key)
            tile_meta = services.checkCache(map_key, type='json')

            if tile_meta is None:
                #fetch fresh tile metadata if none
                import config_creds
                import config
                import ee
                import ee_services

                ## this is where I imagine putting .clip(bbox)...
                geodesic = ee.Geometry.Rectangle(-180, -60, 180, 85)
                bbox = ee.Geometry(geodesic, None, False)

                logging.info('No tile meta, generating new map from %s ' % (ee_assets.layers[key]["asset_id"]))
                image = ee.Image(ee_assets.layers[key]["asset_id"])
                tile_meta = ee_services.getMap(
                    image.mask(image.gt(0)).clip(bbox),
                    ee_assets.layers[key]["viz_params"],
                    key)
                services.cacheResult({
                    "mapid": tile_meta["mapid"],
                    "token":tile_meta["token"]},
                    map_key
                )


            #first try to get it from EE using the mapid/token given
            tile_url = EE_TILE_URL % (
                tile_meta["mapid"], int(z), int(x), int(y), tile_meta["token"])

            logging.info("First try, using cache token -- fetching tile from %s" % tile_url)
            #test that it is an image
            try:
                tile = urlfetch.fetch(tile_url, deadline=60).content
                image = images.Image(image_data = tile)
                if image.format >= 0    :
                    logging.info('caching tile')
                    services.cacheResult(tile, tile_key, type = 'blob')
                    services.writeResult(tile, self.response, format='image/png')
                else:
                    raise Exception('format','Bad format')
            except Exception as e:
                #expired, try again
                import config_creds
                import config
                import ee
                import ee_services

                logging.info('Generating new map from %s ' % (ee_assets.layers[key]["asset_id"]))

                ## this is where I imagine putting .clip(bbox)...
                geodesic = ee.Geometry.Rectangle(-180, -60, 180, 85)
                bbox = ee.Geometry(geodesic, None, False)
                image = ee.Image(ee_assets.layers[key]["asset_id"])
                tile_meta = ee_services.getMap(
                    image.mask(image.gt(0)).clip(bbox),
                    ee_assets.layers[key]["viz_params"],
                    key)

                services.cacheResult({
                    "mapid": tile_meta["mapid"],
                    "token":tile_meta["token"]},
                    map_key
                )
                #first try to get it from EE using the mapid/token given
                tile_url = EE_TILE_URL % (
                    tile_meta["mapid"], int(z), int(x), int(y), tile_meta["token"])
                logging.info("Second Try, using new token - Fetching tile from %s" % tile_url)
                try:
                    tile = urlfetch.fetch(tile_url, deadline=60).content
                    image = images.Image(image_data = tile)
                    if image.format >0:
                        services.cacheResult(tile, tile_key, type = 'blob')
                        services.writeResult(tile, self.response, format='image/png')
                    else:
                        raise Exception ('format',image.format)
                except Exception as e:
                    logging.info(e)
                    services.writeResult(
                        {"error": "Tile not available, we tried!"},
                        self.response, format = 'application/json')



application = webapp2.WSGIApplication([
    webapp2.Route(r'/api/tile/<key>/<z>/<x>/<y>.png',
        handler='tile_handler.TileHandler:get')],
    debug=True)
