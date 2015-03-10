import os
import ee
import config_creds

from oauth2client.appengine import AppAssertionCredentials
from google.appengine.api import urlfetch

# Set up the appropriate credentials depending on where we're running.
if config_creds.DEBUG_MODE:
    EE_CREDENTIALS = ee.ServiceAccountCredentials(config_creds.EE_ACCOUNT, config_creds.EE_PRIVATE_KEY_FILE)
else:
    # The OAuth scope URL for the Google Earth Engine API.
    SCOPES = ('https://www.googleapis.com/auth/earthengine.readonly', 
              'https://www.googleapis.com/auth/earthbuilder.readonly')
    SCOPES = ' '.join(SCOPES)
    EE_CREDENTIALS = AppAssertionCredentials(scope=SCOPES)

ee.Initialize(EE_CREDENTIALS, config_creds.EE_URL)