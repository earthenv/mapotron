mapotron
========

A generic Earth Engine asset viewer.

***Requirements***

_Minimum:_  
* Google AppEngine Python SDK
* Access to an AppEngine application that has access to EarthEngine and the configured MapsEngine assets

_For local development and testing:_
* A Google service account that has been whitelisted to access MapsEngine and EarthEngine
* bower
* grunt

***Setting up a local development server***

1. If you don't have them already, install bower and grunt

  ```
    $ npm install bower
    $ npm install grunt
    $ npm install grunt-contrib-uglify
  ```

2. Install client dependencies

  ```
    $ bower install
  ```

3. Sit down, breath deeply, and relax -- the next part might hurt.  
  
  Install the [Google EarthEngine Python API](https://code.google.com/p/earthengine-api/)
  and follow the instructions for installing its dependencies. You will need to copy the
  python/ee folder into the root of the application, as well as httplib2, and oauth2client.
  You will also need to generate a service account and privatekey.pem file that can
  be used by the application and configure these in config_creds.py
  (see template config_creds.tmpl). More detailed instructions for getting this set up are
  in the [AppEngine hello_world example](https://code.google.com/p/earthengine-api/source/browse/python/examples/AppEngine/hello_world/README.txt)  in the EarthEngine Python API.
  

4. Configure your image assets in ee_assets.py and any legends in app/img/legend

5. Run the application
  
  ```
    $ dev_appserver.py .
  ```
  
  Check to see that it works as advertised at http://localhost:8080/

6. Deploy the application for the world to see.

  ```
    $ appcfg.py . -A my-appengine-app-id -V some-version-name
  ```

  Check to see that it works at http://some-version-name.my-appengine-app-id.appspot.com/

_Notes:_

  * If you make any changes in javascript, you need to recompile the javascript
  
  ```
    $ grunt
  ```
