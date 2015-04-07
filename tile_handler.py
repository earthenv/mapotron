"""
   Module to generate and cache tiles for assets configured in
   ee_assets.
"""

__author__ = "Jeremy Malczyk"

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
MASTER_KEY = 'streams_04072015'
MAP_KEY = MASTER_KEY + '_map_%s' #map configs will be stored behind this key prefix
TILE_KEY = MASTER_KEY + '_tile_%s' #tile blobs will be stored behind this key prefix

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
            tile = open('app/img/empty.png', 'r').read()
            services.writeResult(tile, self.response, format='image/png')

    def getTile(self,key,z,x,y):

        #first try and fetch from cache
        tile_key = TILE_KEY % ('_%s_%i_%i_%i' % (key, int(z), int(x), int(y)))
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
            map_key =  MAP_KEY % (key)
            tile_meta = services.checkCache(map_key, type='json')

            if tile_meta is None:
                #fetch fresh tile metadata if none
                import config_creds
                import config
                import ee
                import ee_services

                
                logging.info('No tile meta, generating new map from %s ' % (ee_assets.layers[key]["asset_id"]))

                tile_meta = ee_services.getMap(
                    ee.Image(ee_assets.layers[key]["asset_id"]),
                    ee_assets.layers[key]["viz_params"],
                    key)


            #first try to get it from EE using the mapid/token given
            tile_url = EE_TILE_URL % (
                tile_meta["mapid"], int(z), int(x), int(y), tile_meta["token"])

            logging.info("First try -- fetching tile from %s" % tile_url)
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

                tile_meta = ee_services.getMap(
                    ee.Image(ee_assets.layers[key]["asset_id"]),
                    ee_assets.layers[key]["viz_params"],
                    key)
                #first try to get it from EE using the mapid/token given
                tile_url = EE_TILE_URL % (
                    tile_meta["mapid"], int(z), int(x), int(y), tile_meta["token"])
                logging.info("Second Try - Fetching tile from %s" % tile_url)
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
