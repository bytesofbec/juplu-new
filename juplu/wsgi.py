import os
import sys
import traceback

def application(environ, start_response):
    try:
        from django.core.wsgi import get_wsgi_application
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'juplu.settings')
        _app = get_wsgi_application()
        return _app(environ, start_response)
    except Exception as e:
        err = traceback.format_exc()
        start_response('500 Internal Server Error', [('Content-Type', 'text/plain')])
        return [err.encode('utf-8')]

