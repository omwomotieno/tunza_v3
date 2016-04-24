from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from services.forms import ServiceForm
import datetime

gestational_period = datetime.timedelta(days=280)


def create(request):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    form = ServiceForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        # messages.success(request, 'Successfully Created')
    context = {'form': form}
    return render(request, 'services/create.html', context)


def profile(request, id=None):
    pass
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Service, id=id)
    context = {'instance_profile': instance_profile, }
    return render(request, 'services/profile.html', context)


def update(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Service, id=id)
    form = ServiceForm(request.POST or None, instance=instance_profile)
    if form.is_valid():
        instance = form.update()
        # message success
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'instance_profile': instance_profile,
        'form': form,
    }
    return render(request, 'services/create.html', context)


def update_2(request, id=None):
    pass
    if not request.user.is_authenticated():
        return render


def delete(request, id=None):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    instance_profile = get_object_or_404(Service, id=id)
    instance_profile.delete()
    return redirect('services:list')


def list(request):
    if not request.user.is_authenticated():
        return render(request, '404.html')
    service_count = Service.objects.count()
    queryset_list = Service.objects.all()

    query = request.GET.get('q')
    if query:
        queryset_list = queryset_list.filter(
            Q(service_name__icontains=query) |
            Q(service_url__icontains=query)
        )
    paginator = Paginator(queryset_list, 6)
    page = request.GET.get('page')
    try:
        service_list = paginator.page(page)
    except PageNotAnInteger:
        service_list = paginator.page(1)
    except EmptyPage:
        service_list = paginator.page(paginator.num_pages)
    context = {
        'service_count': service_count,
        'service_list': service_list,
    }
    return render(request, 'services/list.html', context)
