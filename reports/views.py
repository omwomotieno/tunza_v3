
from django.shortcuts import render
from register.models import Patient
from reminder.models import Appointment_Response, Reminder
from call_engine.models import Call_Response
from services.models import Service


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
    queryset = Patient.objects.all()
    context = {
        'queryset': queryset,
    }
    return render(request, 'reports/patients.html', context)
