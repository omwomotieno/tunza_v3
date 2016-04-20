from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
	list_display = ('service_name','service_about', 'service_url',)
	list_per_page = (8)

admin.site.register(Service, ServiceAdmin)

