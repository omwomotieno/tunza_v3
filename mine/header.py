# You can use mechanize lib from python:

import mechanize
b = mechanize.Browser()

# Set any header you like:
b.addheaders = [('Content-Type', 'application/xml; charset=utf-8')]
response = b.open('http://www.reddit.com')
data = response.read()

# Add:

headers['Content-Type'] = 'application/xml'

# Before instantiating your Request object.