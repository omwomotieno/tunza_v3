from django.conf.urls import url
from call_engine import views

urlpatterns = [
	url(r'^(?P<id>\d+)/call_back/$', views.voice_callback, name='call_back'),
    url(r'^(?P<id>\d+)/current_time/$', views.check_time, name='current_time'),
]
