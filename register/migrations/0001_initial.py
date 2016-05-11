# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-10 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discharged', models.BooleanField(default=False, verbose_name='Active')),
                ('discharge_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anc_number', models.SlugField(max_length=6)),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('creation_date', models.DateField(auto_now=True)),
                ('patient_contact', phonenumber_field.modelfields.PhoneNumberField(help_text='Enter number in this format +2547209XXXXX', max_length=13, unique=True)),
                ('patient_name', models.CharField(max_length=64)),
                ('national_id', models.BigIntegerField(default=None, unique=True)),
                ('last_menstrual_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Patients',
            },
        ),
        migrations.AddField(
            model_name='discharge',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.Patient'),
        ),
    ]
