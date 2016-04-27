from django.http import HttpResponse
from .models import Call_Response
from reminder.models import Appointment_Response
from reminder.models import Reminder
from datetime import timedelta, datetime
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException


# Create your views here.

def voice_callback(request):
    if request.method == 'GET':
        # queryset_response = Appointment_Response.objects.all()
        # queryset_call = Call_Response.objects.all()

        # retrieving service url from contact
        callTo = '+254720955704' # request.GET.get('callerNumber', '')
        call_number = callTo
        patient_contact = Reminder.objects.filter(patient__patient_contact=call_number)
        instance_url = patient_contact.values_list('service__service_url', flat=True)

        isActive = str(1)
        is_active = isActive   #request.GET.get('isActive', '')

        if is_active == str(0):
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say playBeep="false" >Welcome to the reminder system</Say>'
            response += '</Response>'
            resp = HttpResponse(response, content_type='application/xml')
            resp['Cache-Control'] = 'no-cache'
            return resp

        elif is_active == str(1):
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            # response += '<Play url="http://www.kozco.com/tech/piano2-Audacity1.2.5.mp3"/>'
            response += '<Play url="'
            response += instance_url[0]
            response += '"/>'
            response += '</Response>'
            resp = HttpResponse(response, content_type='application/xml')
            resp['Cache-Control'] = 'no-cache'
            return resp

        else:
            resp = HttpResponse('Bad Request', content_type='application/xml', )
            resp['Cache-Control'] = 'no-cache'
            print ('No value was received')
            return resp


def check_time(request, id=None):
    today = datetime.now().date()
    difference = timedelta(days=1)
    call_date = today + difference
    query_set = Reminder.objects.filter(appointment_date=call_date).filter(set_on=True)
    instance = query_set.get(id=60)
    format = '%H:%M'
    instance_contact = instance.patient.patient_contact
    instance_time = instance.time_of_call.strftime(format)
    current_time = datetime.now().time()
    curr_time = current_time.strftime(format)

    print curr_time
    print instance_time
    print instance_contact

    if instance_time == curr_time:
        callTo = instance_contact
        username = "OtisKe"
        apikey = "07984423a278ead54fee35d3daf956598deb51405b27fe70f1e2dfe964be5c04"
        callFrom = "+254711082079"
        message = "We tried calling you to inform you of the appointment. We could not reach you."
        gateway = AfricasTalkingGateway(username, apikey)
        try:
            gateway.call(callFrom, callTo)
            return HttpResponse("Call successfully placed")
        except AfricasTalkingGatewayException, e:
            gateway.sendMessage(callTo, message)
            return HttpResponse("Message sent")
    else:
        return HttpResponse("Not yet Time of Call")


def from_number_to_url(request):
    callTo = '+254700050144'
    call_number = callTo
    # request.GET.get('callerNumber', '')
    patient_contact = Reminder.objects.filter(patient__patient_contact=call_number)
    instance = patient_contact.values_list('service__service_url')
    print instance[0][0]
    return HttpResponse('found')
