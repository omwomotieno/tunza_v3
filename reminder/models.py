from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django import forms
import datetime


# Create your models here.

class Reminder(models.Model):
    patient = models.ForeignKey('register.Patient', on_delete=models.CASCADE,)
    service = models.ForeignKey('services.Service')
    date_created = models.DateField(auto_now = True)
    appointment_date = models.DateField()
    time_of_call = models.TimeField()
    set_on = models.BooleanField(default = True)

    def __unicode__(self):
        return '%s' % self.patient

    def appointment_status(self):
        today = datetime.date.today()
        appointment_date = self.appointment_date
        response = self.response
        if today < appointment_date:
            response = True
        else:
            response = False
        return response

    def date_of_call(self):
        difference = datetime.timedelta(days=1)
        appointment_date = self.appointment_date
        call_date = appointment_date - difference
        return call_date

    def get_absolute_url(self):
        return reverse("reminders:profile", kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = 'Reminders'


class Appointment_Response(models.Model):
    patient = models.ForeignKey(Reminder)
    response_date = models.DateField()
    state = models.BooleanField(default=False)

    def get_patient(self):
        got_patient = self.reminder.patient_id
        return got_patient

    def get_absolute_url(self):
        return reverse("reminders:response", kwargs={"id": self.id})
