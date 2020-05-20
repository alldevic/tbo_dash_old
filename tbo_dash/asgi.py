import os
import socketio

from django.core.asgi import get_asgi_application
from tbo_dash.ws_main.socket_app import sio_app

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tbo_dash.settings')

django_app = get_asgi_application()

application = socketio.ASGIApp(sio_app, 
                                socketio_path="wsdash",
                                other_asgi_app=django_app)
