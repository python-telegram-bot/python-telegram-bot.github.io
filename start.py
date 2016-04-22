import os
import cherrypy
from cherrypy import wsgiserver

from ptb_website import wsgi, settings

from httplogger import HTTPLogger

PATH = os.path.abspath(os.path.dirname(__file__))


class Root(object):
    pass

def make_static_config(static_dir_name):
    """
    All custom static configurations are set here, since most are common, it
    makes sense to generate them just once.
    """
    static_path = os.path.join('/', static_dir_name)
    path = os.path.join(PATH, static_dir_name)
    configuration = {static_path: {
        'tools.staticdir.on': True,
        'tools.staticdir.dir': path}
    }
    
    return cherrypy.tree.mount(Root(), '/', config=configuration)

application = wsgiserver.WSGIPathInfoDispatcher(
{
    '/': wsgi.application,
    settings.STATIC_URL[:-1]: make_static_config(settings.STATIC_URL[1:-1]),
    settings.MEDIA_URL[:-1]: make_static_config(settings.MEDIA_URL[1:-1])
})
    
cherrypy.config.update({'environment': 'production',
                'log.error_file': 'site.log',
                'log.screen': True})

server = wsgiserver.CherryPyWSGIServer(('127.0.0.1', 8001), HTTPLogger(application),
                                       server_name='python-telegram-bot.org')
try:
    server.start()
except KeyboardInterrupt:
    print("Terminating server...")
    server.stop()

