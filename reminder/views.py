from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Reminder, Appointment_Response
from .forms import ReminderForm, AppointmentResponseForm
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


def appointment_response(request):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    form = AppointmentResponseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/users/')
            # messages.success(request, 'Successfully Created')
    context = {'form': form}
    return render(request, 'reminders/response.html', context)


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
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Appointment Successfully Created')
            return HttpResponseRedirect('/reminders/list/')
    context = {'form': form,}
    return render(request, 'reminders/create.html', context)


def update(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Reminder, id=id)
    form = ReminderForm(request.POST or None, instance=instance_profile)
    if form.is_valid():
        instance = form.update(commit=False)
        instance.update()
        # messages.success(request, 'Appointment Successfully Updated')
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
    messages.success(request, 'Appointment Successfully Deleted')
    return redirect('reminders:list')


def list(request):
    '''
    This method counts all the active and discharged reminders specific
    to an expectant mother and returns a list of them
    '''
    if not request.user.is_authenticated():
        return render(request, '404.html')
    reminder_count = Reminder.objects.count()
    queryset_list = Reminder.objects.all().order_by('appointment_date','time_of_call','patient__patient_name')
    # contacts = queryset_list.values_list('patient_id', 'patient__patient_contact')
    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(patient__patient_name__icontains=query)|
            Q(service__service_name__icontains=query)
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
            Q(patient__patient_name=query)|
            Q(appointment_date__exact=query)
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
