from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django import forms
import datetime


# Create your models here.

class Reminder(models.Model):
    TIME = (
        (None, 'Select time of call'),
        ('07:05:00','Morning'),
        ('12:30:00','Midday'),
        ('18:05:00','Evening')
    )
    patient = models.ForeignKey('register.Patient', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service')
    date_created = models.DateField(auto_now = True)
    appointment_date = models.DateField()
    time_of_call = models.CharField(max_length=8, choices=TIME)
    set_reminder = models.BooleanField(default = False)
    response = models.BooleanField(default = False)
    sent_message = models.BooleanField(default = False)

    def __unicode__(self):
        return '%s' % self.time_of_call

    def state_of_reminder(self):
        pass
        set_reminder = self.set_reminder
        if set_reminder == '0':
            pass
        elif set_reminder == '1':
            pass
        return set_reminder

    def response_status(self):
        pass
        response = self.response
        set_reminder = self.set_reminder
        if response == '1':
            set_reminder = False
        elif response == '0':
            set_reminder = True
        return response

    def appointment_status(self):
        today = datetime.date.today()
        appointment_date = self.appointment_date
        set_reminder = self.set_reminder
        if today < appointment_date:
            set_reminder = True
        else:
            set_reminder = False
        return set_reminder

    def get_absolute_url(self):
        return reverse("reminders:profile", kwargs={"id": self.id})

    def date_of_call(self):
        difference = datetime.timedelta(days=1)
        appointment_date = self.appointment_date
        call_date = appointment_date - difference
        return call_date


    # def call_time(self):
    #     time_of_call = self.time_of_call
    #     if time_of_call == 'Morning':
    #         time_of_call = '07:05:00'
    #     elif time_of_call == 'Midday':
    #         time_of_call =
    #     elif time_of_call == 'Evening':
    #         time_of_call = '18:05:00'

    class Meta:
        verbose_name_plural = 'Reminders'
