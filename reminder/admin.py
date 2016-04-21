from django.contrib import admin
from .models import Reminder
from services.models import Service


class ReminderAdmin(admin.ModelAdmin):
	view_on_site = True
	list_display = ('patient', 'date_created', 'appointment_date', 'time_of_call', 'service',
	                'response', 'sent_message',)
	search_fields = ('appointment_date',)
	list_per_page = (6)
	list_editable = ('appointment_date',)

admin.site.register(Reminder, ReminderAdmin)
