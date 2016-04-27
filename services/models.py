from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=64)
    service_about = models.CharField(max_length=512)
    service_url = models.URLField(blank=True, null=True)
    service_file = models.FileField(blank=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Services'


    def __unicode__(self):
        return '%s %s' % self.service_name, self.service_url


    def get_absolute_url(self):
        return reverse("services:profile", kwargs={"id": self.id})
