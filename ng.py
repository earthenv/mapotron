# A handler to render the index.html template for the MOL AngularJS SPA

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import logging
import os
import random
import ee_assets
import webapp2
import json


if 'SERVER_SOFTWARE' in os.environ:
    PROD = not os.environ['SERVER_SOFTWARE'].startswith('Development')
else:
    PROD = True

class BaseHandler(webapp2.RequestHandler):
    def render_template(self, f, template_args):
        path = os.path.join(os.path.dirname(__file__), "server_templates", f)
        self.response.out.write(template.render(path, template_args))

    def push_html(self, f):
        path = os.path.join(os.path.dirname(__file__), "server_templates", f)
        self.response.out.write(open(path, 'r').read())

class ngMOL(BaseHandler):
    def get(self):

	layers = []
	for id in ee_assets.layers.keys():
		layers.append({"id":id, "title":ee_assets.layers[id].get("title") or id})
        self.render_template('index.html', {"layers" : layers, "PROD": PROD})
    def post(self):
        self.push_html('index.html')

application = webapp2.WSGIApplication(
         [ 
          ('/.*',ngMOL),
          ('/', ngMOL)
          ],
         debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
