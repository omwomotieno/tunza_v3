from django.contrib import auth, messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient
from reminder.models import Reminder
from services.models import Service
from .forms import PatientForm
import datetime


def create(request):
    '''Method to create a new expectant mother, register her for reception of
	various services as provided'''
    if not request.user.is_authenticated():
        return render(request, '404.html')
    form = PatientForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {'form': form,}
    return render(request, 'patients/create.html', context)


def update(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    # instance_profile = get_object_or_404(Patient, id=id)
    instance_profile = Patient.objects.get(id=id)
    instance_number = instance_profile.anc_number
    form = PatientForm(request.POST or None, instance=instance_profile)
    if form.is_valid():
        contact_ = instance_profile.patient_contact
        name_ = instance_profile.patient_name
        instance_profile.save()
        return HttpResponseRedirect(instance_profile.get_absolute_url())

    context = {
        'instance_profile': instance_profile,
        'form': form,
    }
    return render(request, 'patients/create.html', context)


def delete(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Patient, id=id)
    instance_profile.delete()
    # message success
    return redirect('patients:list')


def list(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    patient_count = Patient.objects.count()
    queryset_list = Patient.objects.all()
    queryset_order = queryset_list.order_by('patient_name')

    query = request.GET.get('q')
    if query:
        queryset_order = queryset_order.filter(
            Q(anc_number__icontains=query) |
            Q(patient_contact__icontains=query) |
            Q(patient_name__icontains=query)
        )

    paginator = Paginator(queryset_order, 10)
    page = request.GET.get('page')
    try:
        patient_list = paginator.page(page)
    except PageNotAnInteger:
        patient_list = paginator.page(1)
    except EmptyPage:
        patient_list = paginator.page(paginator.num_pages)

    context = {
        'patient_list': patient_list,
        'patient_count': patient_count,
    }
    return render(request, 'patients/list.html', context)


def profile(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Patient, id=id)
    # instance_weight = get_object_or_404(Weight, id=instance_profile.id)
    lmd = instance_profile.last_menstrual_date
    format = '"%m/%d/%Y'
    edd = lmd + datetime.timedelta(days=280)
    today = datetime.datetime.now().date()
    # service_list = Service.objects.all()
    # service_scheduled = service_list.filter(reminder__patient=instance_profile)
    # days_to_delivery =  datetime.datetime.strftime((edd - today), format)
    reminder_list = Reminder.objects.all()
    appointment = reminder_list.filter(patient=instance_profile)
    context = {
        'instance_profile': instance_profile,
        'instance_edd': edd,
        # 'instance_delivery': days_to_delivery,
        'appointment': appointment,
        # 'service_scheduled': service_scheduled,
        # 'appointments': appointments,
    }
    return render(request, 'patients/profile.html', context)
