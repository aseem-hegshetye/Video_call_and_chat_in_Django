from django.urls import path

from chat.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<room_name>/',RoomView.as_view(),name='room'),
]
