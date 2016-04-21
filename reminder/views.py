from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reminder
from .forms import ReminderForm
import datetime

gestational_period = datetime.timedelta(days=280)


def profile(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Reminder, id=id)
    rem_date_filter = instance_profile.appointment_date
    today = datetime.datetime.today()
    rem_date = rem_date_filter - datetime.timedelta(days=1)
    # days_rem = rem_date - today
    context = {
        'instance_profile': instance_profile,
        # 'days_rem': days_rem,
        'rem_date': rem_date,
    }
    return render(request, 'reminders/profile.html', context)


def create(request):
    '''
    This view creates a new schedule. It captures the patient id, links
    the id to a scheduled objects and passes it to count down. Creates a
    new patient schedule or reminder. It also starts counting down to the
    1 day to reminder date
    '''
    if not request.user.is_authenticated():
        return render(request, '404.html')
    form = ReminderForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid:
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
            # messages.success(request, 'Successfully Created')
    context = {'form': form}
    return render(request, 'reminders/create.html', context)


def update(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Reminder, id=id)
    form = ReminderForm(request.POST or None, instance=instance_profile)
    if form.is_valid():
        instance = form.update(commit=False)
        instance.update()
        # message success
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'instance_profile': instance_profile,
        'form': form,
    }
    return render(request, 'reminders/create.html', context)


def delete(request, id=None):
    '''
    This method removes a previously set reminder
    '''
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Reminder, id=id)
    instance_profile.delete()
    return redirect('reminders:list')


def list(request):
    '''
    This method counts all the active and discharged reminders specific
    to an expectant mother and returns a list of them
    '''
    if not request.user.is_authenticated():
        return render(request, '404.html')
    reminder_count = Reminder.objects.count()
    queryset_list = Reminder.objects.all().order_by('-date_created')
    # contacts = queryset_list.values_list('patient_id', 'patient__patient_contact')
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(appointment_date__day=query)
        )
    paginator = Paginator(queryset_list, 8)
    page = request.GET.get('page')
    try:
        reminder_list = paginator.page(page)
    except PageNotAnInteger:
        reminder_list = paginator.page(1)
    except EmptyPage:
        reminder_list = paginator.page(paginator.num_pages)

    context = {
        'reminder_list': reminder_list,
        'reminder_count': reminder_count,
        # 'contacts': contacts,
    }
    return render(request, 'reminders/list.html', context)


def response(request):
    pass


def tomorrow(request):
    '''
    This function retrieves all the reminders that are due tomorrow and returns
    the list to the user detail (admin) page.
    '''
    difference = datetime.timedelta(days=1)
    today = datetime.date.today()
    call_day = today + difference
    reminder_service = Reminder.objects.values_list('service_id', 'patient_id',
                                                    'service__service_url', 'patient__patient_contact')
    queryset = Reminder.objects.all()
    tomorrow_list = queryset.filter(
        appointment_date=call_day).order_by('time_of_call')
    tomorrow_count = tomorrow_list.count()
    query = request.GET.get('q')
    if query:
        tomorrow_list = tomorrow_list.filter(
            Q(reminder_date__day=query)
        )
    paginator = Paginator(tomorrow_list, 6)
    page = request.GET.get('page')
    try:
        tomorrow_list = paginator.page(page)
    except PageNotAnInteger:
        tomorrow_list = paginator.page(1)
    except EmptyPage:
        tomorrow_list = paginator.page(paginator.num_pages)
    # contact_list = tomorrow_list.filter(patient__patient_contact=)
    context = {
        'tomorrow_list': tomorrow_list,
        'tomorrow_count': tomorrow_count,
        'reminder_service': reminder_service,
        'queryset': queryset,
    }
    return render(request, 'reminders/incoming.html', context)


def voice_callback(request):
    if request.method == 'GET':

        isActive = str(1)

        link_file = 'http://www.myvoicemailserver.com/audio/vmail.wav'

        is_active = isActive  # request.GET.get('isActive', '')

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
            response += '<Play url="'
            response += link_file
            response += '"/>'
            response += '</Response>'
            resp = HttpResponse(response, content_type='application/xml')
            resp['Cache-Control'] = 'no-cache'
            return resp

    else:
        resp = HttpResponse(
            'Bad Request', content_type='application/xml', )
        resp['Cache-Control'] = 'no-cache'
        print ('No value was received')
        return resp


def check_time(request, pk=None):
    reminder_list = Reminder.objects.get(pk=1)
    reminder_time = reminder_list
    format = '%I:%M'
    current_time = datetime.datetime.now().time()
    curr_time = current_time.strftime(format)

    return HttpResponse(reminder_time)

    # for rem in reminder_time:
    #     try:
    #         reminder_service_name = Reminder.objects.values('service__service_name')
    #         return HttpResponse(reminder_service_name)
    #     except ObjectDoesNotExist:
    #         return HttpResponse('Object not found')
