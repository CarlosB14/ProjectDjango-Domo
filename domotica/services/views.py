from django.shortcuts import render
from .models import (Services, Service)

def services_list(request):
    all_services = Services.objects.all()
    context = {
        'services': all_services
    }
    return render(request, 'services/services_list.html', context)

def services_plan(request, id):
    services_plan = Services.objects.get(pk=id)
    context = {
        'service_plan': services_plan
    }
    return render(request, 'services/service_detail.html', context)

def service_detail(request, id):
    service_detail = Service.objects.get(pk=id)
    context = {
        'service_detail': service_detail
    }
    return render(request, 'services/service_detail.html', context)
    