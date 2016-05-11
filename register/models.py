from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse
import uuid
import datetime


class Patient(models.Model):
    anc_number = models.SlugField(max_length=6)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    creation_date = models.DateField(auto_now=True)
    patient_contact = PhoneNumberField(max_length=13, unique=True,
                                       help_text="Enter number in this format +2547209XXXXX")
    patient_name = models.CharField(max_length=64)
    national_id = models.BigIntegerField(default=None, unique=True)
    last_menstrual_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Patients'

    def __unicode__(self):
        return '%s' % self.patient_name

    def last_menstrual(self):
        today = datetime.date.today()
        last_menstrual_date = self.last_menstrual_date
        if last_menstrual_date > today:
            raise ValueError
        else:
            return last_menstrual_date

    def get_absolute_url(self):
        return reverse("patients:profile", kwargs={"id": self.id})


class Discharge(models.Model):
    patient = models.ForeignKey(Patient)
    discharged = models.BooleanField(default=False, verbose_name='Active')
    # discharge_date = models.DateField(blank=True, auto_now=True)

    class Meta:
        verbose_name_plural = 'Discharge'

    def __unicode__(self):
        return '%s' % self.patient.patient_name
