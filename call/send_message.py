#!/usr/bin/python2.7

from django.http import HttpResponseRedirect, HttpResponse
from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException

# Specify your login credentials
username = "OtisKe"

apikey = "07984423a278ead54fee35d3daf956598deb51405b27fe70f1e2dfe964be5c04"

# Specify the phone numbers in international format
callFrom = "+254711082079"
callTo = "+254720955704"

# Specify the message to be sent incase of any connection errors
message = "We tried calling you but we could not reach you"

# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)

try:
    results = gateway.call(callFrom, callTo)
except AfricasTalkingGatewayException, e:
    results = gateway.sendMessage(callTo, message)
