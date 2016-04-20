#!/usr/bin/python2.7
from django.http import HttpResponse
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from reminder.models import Reminder
import sys
import os
import django

sys.path.append("/home/foxtrot/Dropbox/tunza_v2/")
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
django.setup()

username = "OtisKe"

apikey = "07984423a278ead54fee35d3daf956598deb51405b27fe70f1e2dfe964be5c04"

gateway = AfricasTalkingGateway(username, apikey)

# replace this line with a list of numbers from the
# patient__patient_contact linked to reminder model
reminder_service = Reminder.objects.values_list('service_id',
                                                'patient_id',
                                                'service__service_name',
                                                'service__service_url',
                                                'patient__patient_contact', )


# replace this message with service about from service__service_about
# linked to reminder model


def voice_callback(request):
    if request.method == 'POST':
        is_active = request.values.get('isActive', None)
        session_id = request.values.get('sessionId', None)
        caller_number = request.values.get('callerNumber', None)
        direction = request.values.get('direction', None)

        print "is_active -> ", is_active

        if is_active == str(0):
            # Compose the response
            duration = request.values.get('durationInSeconds', None)
            currency_code = request.values.get('currencyCode', None)
            amount = request.values.get('amount', None)
            # update session info to Redis

            print duration, currency_code, amount

            respond = '<?xml version="1.0" encoding="UTF-8"?>'
            respond += '<Response>'
            respond += '<Say playBeep="false" >Welcome to the reminder system</Say>'
            respond += '</Response>'

            resp = HttpResponse(respond, 200, content_type='application/xml')
            resp['Cache-Control'] = 'no-cache'
            return resp

        if is_active == str(1):
            # Compose the response
            respond = '<?xml version="1.0" encoding="UTF-8"?>'
            respond += '<Response>'
            respond += '<Say playBeep="false" >Welcome to mTunza.org</Say>'
            respond += '</Response>'

            resp = HttpResponse(respond, 200, content_type='application/xml')
            resp['Cache-Control'] = 'no-cache'
            return resp

    else:
        resp = HttpResponse('Bad Request', 400, content_type='application/xml', )
        resp['Cache-Control'] = 'no-cache'
        return resp
