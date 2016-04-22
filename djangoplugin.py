# -*- coding: utf-8 -*-
import imp
import os, os.path

import cherrypy
from cherrypy.process import plugins

from django.conf import settings
from django.core.handlers.wsgi import WSGIHandler

from httplogger import HTTPLogger

__all__ = ['DjangoAppPlugin']

class DjangoAppPlugin(plugins.SimplePlugin):
    def __init__(self, bus, application, settings_module, wsgi_http_logger=HTTPLogger):
        """ CherryPy engine plugin to configure and mount
        the Django application onto the CherryPy server.
        """
        plugins.SimplePlugin.__init__(self, bus)
        
        self.application = application
        self.settings = settings_module
        self.wsgi_http_logger = wsgi_http_logger

    def start(self):
        """ When the bus starts, the plugin is also started
        and we load the Django application. We then mount it on
        the CherryPy engine for serving as a WSGI application.
        We let CherryPy serve the application's static files.
        """
        
        cherrypy.log("Loading and serving the Django application")
        
        cherrypy.tree.graft(self.wsgi_http_logger(self.application), '/')
        # cherrypy.tree.graft(self.application, '/')
        
        
