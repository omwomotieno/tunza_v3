from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=64)
    service_about = models.CharField(max_length=512)
    service_url = models.URLField(blank=True, null=True, unique=True)
    service_field = models.FileField(upload_to='service_files')
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Services'


    def __unicode__(self):
        return '%s' % self.service_name


    def get_absolute_url(self):
        return reverse("services:profile", kwargs={"id": self.id})
