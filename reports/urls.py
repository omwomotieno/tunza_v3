from django.conf.urls import url, patterns
from reports import views

urlpatterns=[
    url(r'^appointment_report/$', views.AppointmentReports, name='appointment_report'),
    url(r'^call_report/$', views.CallReports, name='call_report'),
    url(r'^patient_report/$', views.PatientReports, name='patient_report'),
    url(r'^reminder_report/$', views.AppointmentResponseReports, name='response_report'),
    url(r'^service_report/$', views.ServiceReports, name='service_report'),
]
