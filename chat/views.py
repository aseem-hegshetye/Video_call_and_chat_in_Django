from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'chat/index.html'


class RoomView(TemplateView):
    template_name = 'chat/room.html'

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context['room_name'] = self.request.GET.get('room_name')
        return context


