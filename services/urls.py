from django.conf.urls import url
from services import views

urlpatterns = [
	# service configurations
	url(r'^(?P<id>\d+)/$', views.profile, name='profile'),
	url(r'^create/', views.create, name='create'),
	url(r'^(?P<id>\d+)/delete/$', views.delete, name='delete'),
	url(r'^(?P<id>\d+)/edit/$', views.update, name='update'),
	url(r'^list/', views.list, name='list'),
 ]
