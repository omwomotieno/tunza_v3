from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=64, unique=True)
    service_about = models.CharField(max_length=512)
    service_url = models.URLField(blank=True, null=True, unique=True, help_text='This link should be unique')
    service_msg = models.CharField(blank=True, null=True, max_length=160,
                                   default='We tried caling you. AMUA Clinic',
                                   help_text='Optional message to be sent')
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Services'


    def __unicode__(self):
        return '%s' % self.service_name


    def get_absolute_url(self):
        return reverse("services:profile", kwargs={"id": self.id})
