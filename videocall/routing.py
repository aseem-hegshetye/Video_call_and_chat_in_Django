# chat/routing.py
from django.urls import path

from videocall.consumers import *

websocket_urlpatterns = [
    path(r'ws/video_call/signal/', VideoCallSignalConsumer),
]
