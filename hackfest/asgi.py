"""
ASGI config for hackfest project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels import routing
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application
from django.urls import re_path

from device.routing import websocket_urlpatterns
from device.views import StreamConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hackfest.settings')



a= [
        re_path("ws/", StreamConsumer.as_asgi()),
        re_path("socket.io/", StreamConsumer.as_asgi()),
    ]

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)

    "websocket": AuthMiddlewareStack(
        URLRouter(
            a
        )
    ),
})
