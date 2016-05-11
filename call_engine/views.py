from datetime import timedelta, datetime
from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from django_cron import CronJobBase, Schedule
from .models import Call_Response
from reminder.models import Reminder
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException


# Create your views here.

def voice_callback(request):
    current_time = datetime.now().time()
    time_format = '%H:%M'
    curr_time = current_time.strftime(time_format)

    username = "OtisKe"
    apikey = "07984423a278ead54fee35d3daf956598deb51405b27fe70f1e2dfe964be5c04"
    gateway = AfricasTalkingGateway(username, apikey)

    if request.method == 'GET':
        # queryset_response = Appointment_Response.objects.all()
        # queryset_call = Call_Response.objects.all()

        # retrieving call_back params
        is_active = str(1)  # request.GET.get('isActive', '')
        callTo = '+254720955704'  # request.GET.get('callerNumber', '')

        # retrieving service url and msg from callerNumber

        patient_contact = Reminder.objects.filter \
            (patient__patient_contact=callTo).filter(time_of_call=curr_time)
        instance_url = patient_contact.values_list('service__service_url', flat=True)
        instance_msg = patient_contact.values_list('service__service_msg', flat=True)
        print instance_msg
        if is_active == str(0):
            try:
                gateway.sendMessage(callTo, instance_msg)
            except AfricasTalkingGatewayException, e:
                response = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Say playBeep="false" >Thank you</Say>'
                response += '</Response>'
                resp = HttpResponse(response, content_type='application/xml')
                resp['Cache-Control'] = 'no-cache'
                return resp

        elif is_active == str(1):
            # set call_response to True
            try:
                response = '<?xml version="1.0" encoding="UTF-8"?>'
                response += '<Response>'
                response += '<Play url="'
                response += instance_url[0]
                response += '"/>'
                response += '</Response>'
                resp = HttpResponse(response, content_type='application/xml')
                resp['Cache-Control'] = 'no-cache'
                return resp
            except AfricasTalkingGatewayException, e:
                print e

        else:
            resp = HttpResponse('Bad Request', content_type='application/xml', )
            resp['Cache-Control'] = 'no-cache'
            print ('No value was received')
            return resp


class TunzaCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'tunza.TunzaCronJob'

    def do(self):
        username = "OtisKe"
        apikey = "07984423a278ead54fee35d3daf956598deb51405b27fe70f1e2dfe964be5c04"
        callFrom = "+254711082079"
        gateway = AfricasTalkingGateway(username, apikey)

        today = datetime.now().date()
        difference = timedelta(days=1)
        call_date = today + difference

        current_time = datetime.now().time()
        time_format = '%H:%M'
        curr_time = current_time.strftime(time_format)

        query_set = get_list_or_404(
            Reminder,
            appointment_date=call_date,
            set_on=True,
            time_of_call=curr_time,
        )

        for instance in query_set:
            instance_contact = instance.patient.patient_contact
            callTo = instance_contact
            gateway.call(callFrom, callTo)

        return HttpResponse("Calls successfully placed")
