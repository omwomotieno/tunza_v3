from django.conf.urls import url
from reminder import views

urlpatterns = [
    # schedule configurations
    url(r'^profile/(?P<id>\d+)/$', views.profile, name='profile'),
    url(r'^create/', views.create, name='create'),
    url(r'^delete/(?P<id>\d+)/delete/$', views.delete, name='delete'),
    url(r'^update/(?P<id>\d+)/edit/$', views.update, name='update'),
    url(r'^list/', views.list, name='list'),
    url(r'^list-tomorrow/$', views.tomorrow, name='tomorrow'),
    url(r'^callback/$', views.voice_callback, name='callback'),
    url(r'^current_time/$', views.check_time, name='current_time'),
]
