# Register MOL backend services here, then put their
# scripts and sql in the appropriate services sub-folder

# speciesinfo service runs speciesinfo.sql
# against the cartodb sql api in the /services/cartodb folder

import logging
import cache
import json
import hashlib
import config_creds

from collections import OrderedDict

from google.appengine.api import taskqueue
from google.appengine.api import memcache
#EE_TILE_URL = '/api/tile/%s/{Z}/{X}/{Y}/%s' # (key, token)
EE_TILE_URL = 'https://earthengine.googleapis.com/map/%s/{Z}/{X}/{Y}?token=%s'



def getKey(endpoint, querystring):
    return '%s_%s_%s' % (
        cache_key,
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
            logging.info('No json in memcache, checking cache')
            result = cache.get(key, value_type='string', loads=True)
    else:
        result = memcache.get(key)
        if result:
            logging.info('Got something from memcache')
        else:
            logging.info('No blob in memcache, checking cache')
            result = cache.get(key, value_type='blob')

    if result is not None:
        logging.info("Got something from cache for %s." % key)
    else:
        logging.info("No love in cache for %s." % key)

    return result


def cacheResult(result, key, type='json'):
    logging.info('Caching %s' % key)
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
        logging.info(type(result))
        if type(result) not in ( type(str()), type(unicode())):
            response.out.write(json.dumps(result))
        else:
            response.out.write(result)
    elif format == "csv":
        response.headers["Content-Type"] = "text/csv"
        response.headers["Content-Disposition"] = str("attachment; filename=%s" % str(filename))
        response.out.write(result)
    else:
        response.out.write(result)
