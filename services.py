"""

   Some generic cache management functions.

"""

__author__ = "Jeremy Malczyk"

import logging
import cache
import json
import hashlib
import config_creds
import ee_assets

from google.appengine.api import taskqueue
from google.appengine.api import memcache


cache_key = "021920151211_%s_%s"

EE_TILE_URL = 'https://earthengine.googleapis.com/map/%s/{Z}/{X}/{Y}?token=%s'


def getKey(endpoint, querystring):
    return cache_key % (
        endpoint,
        hashlib.md5(
            querystring
        ).hexdigest()
    )



def checkCache(key, type='json'):
    logging.info('Checking cache for %s' % (key))

    if type == 'json':
        result = memcache.get(key)
        if result:
            result = json.loads(result)
        else:
            result = cache.get(key, value_type='string', loads=True)
    else:
        result = memcache.get(key)
        if result is None:
            result = cache.get(key, value_type='blob')

    if result is not None:
        logging.info("Got something from cache.")
    else:
        logging.info("No love in cache.")

    return result


def cacheResult(result, key, type='json'):
    if type == 'json':
        cache.add(key, json.dumps(result), value_type='string')
        memcache.add(key, json.dumps(result))
    else:
        cache.add(key, result, value_type='blob')
        memcache.add(key, result)


def writeResult(result, response, format="application/json", filename="mol.csv"):
    response.headers["Content-Type"] = format
    if format == "application/json":
        response.headers["Content-Type"] = "application/json"
        response.out.write(json.dumps(result))
    elif format == "csv":
        response.headers["Content-Type"] = "text/csv"
        response.headers["Content-Disposition"] = str("attachment; filename=%s" % str(filename))
        response.out.write(result)
    else:
        response.out.write(result)
