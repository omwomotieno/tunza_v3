# chartit

from django.shortcuts import render
from chartit import DataPool, Chart

# graphos
from graphos.sources.simple import SimpleDataSource
from graphos.sources.model import ModelDataSource
from graphos.renderers import flot

from register.models import Patient
from reminder.models import Appointment_Response, Reminder
from call_engine.models import Call_Response
from services.models import Service


# from vitals.models import


# Create your views here.

# def PatientReports(request):
#     pass
#     query_set = Patient.objects.all()
#     context = {
#
#     }
#     return render(request, 'reports/patients.html', context)
#

def AppointmentReports(request):
    pass
    query_set = Reminder.objects.all()
    context = {

    }
    return render(request, 'reports/appointments.html', context)


def AppointmentResponseReports(request):
    pass
    query_set = Appointment_Response.objects.all()
    context = {

    }
    return render(request, 'reports/appointment_response.html', context)


def CallReports(request):
    pass
    query_set = Call_Response.objects.all()
    context = {

    }
    return render(request, 'reports/call_response.html', context)


def ServiceReports(request):
    pass
    query_set = Service.objects.all()
    context = {

    }
    return render(request, 'reports/services.html', context)


def PatientReports(request):
    queryset = Patient.objects.all()
    data_source = ModelDataSource(queryset, fields=['patient_name', 'anc_number'])
    chart = flot.LineChart(data_source, options={'series': {'color': 'orange'},
                                                 'lines': {'lineWidth': 2, 'fill': 1, 'fillColor': {
                                                     'colors': ["rgba(0, 0, 153, 0.4)", "rgba(255, 255, 255,0.4)"]}},
                                                 'points': {'symbol': 'circle'},
                                                 'xaxis': {'mode': 'time', 'timezone': 'browser',
                                                           'axisLabel': 'Date Time', 'axisLabelUseCanvas': 'true',
                                                           'axisLabelFontSizePixels': 20,
                                                           'axisLabelFontFamily': 'Arial', 'color': 'red'},
                                                 'yaxis': {'min': 50, 'max': 400, 'tickSize': 50,
                                                           'axisLabel': 'Centimeters', 'axisLabelUseCanvas': 'true',
                                                           'axisLabelFontSizePixels': 20,
                                                           'axisLabelFontFamily': 'Arial'}, 'grid': {'color': 800}})
    context = {
        'chart': chart,
    }
    return render(request, 'reports/patients.html', context)
