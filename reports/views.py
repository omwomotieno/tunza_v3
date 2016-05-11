from django.shortcuts import render
from django.db.models import Count
from register.models import Patient
from reminder.models import Appointment_Response, Reminder
from call_engine.models import Call_Response
from services.models import Service

import arrow


def AppointmentReports(request):
    query_set = Reminder.objects.all()
    context = {
        'queryset': query_set,

    }
    return render(request, 'reports/appointments.html', context)


def AppointmentResponseReports(request):
    query_set = Appointment_Response.objects.all()
    context = {

    }
    return render(request, 'reports/appointment_response.html', context)


def CallReports(request):
    query_set = Call_Response.objects.all()
    context = {

    }
    return render(request, 'reports/call_response.html', context)


def ServiceReports(request):
    query_set = Service.objects.all()
    context = {

    }
    return render(request, 'reports/services.html', context)


def PatientReports(request):
    final_data = []

    list = Patient.objects.values('creation_date').count()
    context = {

        'pat_reg': final_data,
        'list': list,
    }
    return render(request, 'reports/patients.html', context)
