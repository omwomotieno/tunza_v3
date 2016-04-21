from django.conf.urls import url
from call_engine import views

urlpatterns = [
	url(r'^call_back/$', views.voice_callback, name='call_back'),
    url(r'^current_time/$', views.check_time, name='current_time'),
]
