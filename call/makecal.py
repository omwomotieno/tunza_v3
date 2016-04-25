#!/usr/bin/python2.7
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
# import sys
# import os
# import django
#
# sys.path.append("/home/foxtrot/Dropbox/tunza_v2/")
# os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings.local"
# django.setup()
#
# from reminder.models import Reminder
#
# reminder_contacts = Reminder.objects.values_list('patient_id', 'patient__patient_contact')

# Specify your login credentials
username = "OtisKe"

apikey = "07984423a278ead54fee35d3daf956598deb51405b27fe70f1e2dfe964be5c04"

# Specify your Africa's Talking phone number in international format
callFrom = "+254711082079"

# Specify the numbers that you want to call to in a comma-separated list
# Please ensure you include the country code (+254 for Kenya in this case)
callTo = "+254700050144"

# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)

try:
# Make the call
    results = gateway.call(callFrom, callTo)

    for result in results:
# Only status "Queued" means the call was successfully placed
        print "Status : %s; phoneNumber : %s " % (result['status'],
                                                  result['phoneNumber'])
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while making the call: %s' % str(e)
