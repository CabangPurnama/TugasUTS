from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os
from datetime import datetime
from tempfile import NamedTemporaryFile


def export(request):
    response = Response(content_type='application/csv')
    with NamedTemporaryFile(prefix='XML_Export_%s' % datetime.now(),
                            suffix='.xml', delete=True) as f:
        # this is where I usually put stuff in the file
        response = FileResponse(os.path.abspath(f.name))
        response.headers['Content-Disposition'] = ("attachment; filename=Cars.xml")
        return response

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('Cars', '/')
        config.add_view( route_name='Cars')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()
