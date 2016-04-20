#!/usr/bin/python2.7

import sys
import os
import django

sys.path.append("/home/foxtrot/Dropbox/tunza_v2/")
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
django.setup()

from reminder.models import Reminder

reminder_contacts = Reminder.objects.values_list('patient_id', 'patient__patient_contact')

for reminder in reminder_contacts:
    print '%s' % reminder
