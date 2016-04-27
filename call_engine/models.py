from __future__ import unicode_literals
from reminder.models import Reminder
from django.db import models

# Create your models here.

class Call_Response(models.Model):
    reminder = models.ForeignKey(Reminder)
    call_date = models.DateTimeField(auto_now_add=True)
    call_response = models.BooleanField(default=False)
