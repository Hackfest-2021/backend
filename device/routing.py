
from django.urls import re_path

from device.views import StreamConsumer

websocket_urlpatterns = [
    re_path("stream/", StreamConsumer.as_asgi()),
]