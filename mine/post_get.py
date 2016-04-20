hello_get.py?first_name = ABC & last_name = XYZ

#!/usr/bin/python

# Import modules for CGI handling
import cgi
import cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

-------------------------------------------

# suppose you're posting a html form with this:

<input type = "text" name = "username" >

# If using raw cgi:

import cgi
form = cgi.FieldStorage()
print form["username"]

# If using Django, Pylons, Flask or Pyramid:

print request.GET['username']  # for GET form method
print request.POST['username']  # for POST form method

------------------------------------------------------

# They are stored in the CGI fieldstorage object.

import cgi
form = cgi.FieldStorage()

print "The user entered %s" % form.getvalue("uservalue")


-------------------------------------------------------
# Here's the Python routine to populate a GET dictionary:

GET = {}
args = os.getenv("QUERY_STRING").split('&')

for arg in args:
    t = arg.split('=')
    if len(t) > 1:
        k, v = arg.split('=')
        GET[k] = v

# and for POST:

POST = {}
args = sys.stdin.read().split('&')

for arg in args:
    t = arg.split('=')
    if len(t) > 1:
        k, v = arg.split('=')
        POST[k] = v
# You can now access the fields as following:

print GET.get('user_id')
print POST.get('user_name')
# I must also point out that the cgi module doesn't work well.
# Consider this HTTP request:

POST / test.py?user_id = 6

user_name = Bob & age = 30

# Using cgi.FieldStorage().getvalue('user_id') will cause
# a null pointer exception because the module blindly checks
# the POST data, ignoring the fact that a POST request can
# carry GET parameters too.

-----------------------------------------------------------
