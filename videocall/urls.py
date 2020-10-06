from django.urls import path

from videocall.views import *

urlpatterns = [
    path('video_call/', VideoCall.as_view(), name='video_call'),
]
