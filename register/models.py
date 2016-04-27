from __future__ import unicode_literals
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.urlresolvers import reverse
import uuid
import datetime


class Patient(models.Model):
    anc_number = models.SlugField(max_length=6)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    creation_date = models.DateTimeField(auto_now=True)
    patient_contact = PhoneNumberField(max_length=13, unique=True,
                                       help_text="Enter number in this format +2547209XXXXX")
    patient_name = models.CharField(max_length=64)
    national_id = models.BigIntegerField(default=None, unique=True)
    last_menstrual_date = models.DateField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Patients'

    def __unicode__(self):
        return '%s' % self.patient_name

    def modify_contact(self):
        contact = '+' + self.patient_contact
        return contact

    def last_menstrual(self):
        today = datetime.date.today()
        last_menstrual_date = self.last_menstrual_date
        if last_menstrual_date > today:
            return '%s' % 'last menstrual date cannot be greater than today'
            # raise ValidationError
        else:
            return last_menstrual_date


    def get_absolute_url(self):
        return reverse("patients:profile", kwargs={"id": self.id})

#
# class Note(models.Model):
#   patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#   service = models.ForeignKey('reminder.Service')
#   note = models.ForeignKey('register.Week')
#   clinical_note = models.TextField()
#   date_created = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#   def get_absolute_url(self):
#       return reverse("patient:note", kwargs={"id": self.id})
#
#   class Meta:
#       verbose_name_plural = 'Notes'
#
#
# class Weight(models.Model):
#   patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#   week = models.ForeignKey('register.Week')
#   weight = models.IntegerField()
#   date_of_input = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#   def get_absolute_url(self):
#       return reverse("patient:weight", kwargs={"id": self.id})
#
#   class Meta:
#       verbose_name_plural = 'Weight'
#
#
# class BP(models.Model):
#   patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
#   week = models.ForeignKey('register.Week')
#   diastole = models.IntegerField(default='000')
#   systole = models.IntegerField(default='00')
#   date_of_input = models.DateTimeField(auto_now=True, auto_now_add=False)
#
#   def get_absolute_url(self):
#       return reverse("patient:bp", kwargs={"id": self.id})
#
#   class Meta:
#       verbose_name_plural = 'Blood Pressure'
#
#
# class Week(models.Model):
#   WEEKS = (
#       ('Week 1', 'Week 1'), ('Week 2', 'Week 2'), ('Week 3', 'Week 3'), ('Week 4', 'Week 4'),
#       ('Week 5', 'Week 5'), ('Week 6', 'Week 6'), ('Week 7', 'Week 7'), ('Week 8', 'Week 8'),
#       ('Week 9', 'Week 9'), ('Week 10', 'Week 10'), ('Week 11', 'Week 11'), ('Week 12', 'Week 12'),
#       ('Week 13', 'Week 13'), ('Week 14', 'Week 14'), ('Week 15', 'Week 15'), ('Week 16', 'Week 16'),
#       ('Week 17', 'Week 17'), ('Week 18', 'Week 18'), ('Week 19', 'Week 19'), ('Week 20', 'Week 20'),
#       ('Week 21', 'Week 21'), ('Week 22', 'Week 22'), ('Week 23', 'Week 23'), ('Week 24', 'Week 24'),
#       ('Week 25', 'Week 25'), ('Week 26', 'Week 26'), ('Week 27', 'Week 27'), ('Week 28', 'Week 28'),
#       ('Week 29', 'Week 29'), ('Week 30', 'Week 30'), ('Week 31', 'Week 31'), ('Week 32', 'Week 32'),
#       ('Week 33', 'Week 33'), ('Week 34', 'Week 34'), ('Week 35', 'Week 35'), ('Week 36', 'Week 36'),
#       ('Week 37', 'Week 37'), ('Week 38', 'Week 38'), ('Week 39', 'Week 39'), ('Week 40', 'Week 40'),
#   )
#   week = models.CharField(max_length=6, choices=WEEKS, unique=True)
#
#   class Meta:
#       verbose_name_plural = 'Weeks'
#
#   def unique_weekly(self):
#       pass
