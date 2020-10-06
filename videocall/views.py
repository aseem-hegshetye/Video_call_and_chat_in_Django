from django.views.generic import TemplateView


class VideoCall(TemplateView):
    template_name = 'videocall/video_call.html'
