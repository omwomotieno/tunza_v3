# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_auto_20160424_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_file',
            field=models.FileField(blank=True, upload_to=b''),
        ),
    ]
