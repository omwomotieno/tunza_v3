from django.conf.urls import url
from register import views

urlpatterns = [
	url(r'^list/', views.list, name='list'),
	url(r'^(?P<id>\d+)/$', views.profile, name='profile'),

    # Patient manipulations
	url(r'^(?P<id>\d+)/edit/$', views.update, name='update'),
	url(r'^(?P<id>\d+)/delete/$', views.delete, name='delete'),
	url(r'^create/', views.create, name='create'),
]
