from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("path/to/consumer/$", consumers.Consumers.as_asgi()),
]
