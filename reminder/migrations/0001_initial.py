# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-21 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateField(auto_now=True)),
                ('appointment_date', models.DateField()),
                ('time_of_call', models.TimeField()),
                ('response', models.BooleanField(default=False)),
                ('sent_message', models.BooleanField(default=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Patient')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.Service')),
            ],
            options={
                'verbose_name_plural': 'Reminders',
            },
        ),
    ]
