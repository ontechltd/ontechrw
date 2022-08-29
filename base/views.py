from django.shortcuts import render
from .models import Service

# Create your views here.

def home(request):
    services = Service.objects.all()
    print(services.count())
    context = {'services':services}
    return render(request, 'base/home.html', context)

def about_us(request):
    
    context = {}
    return render(request, 'base/about-us.html', context)

def services(request):
    services = Service.objects.all()
    context = {'services':services}
    return render(request, 'base/services.html', context)

def contact_us(request):
    
    context = {}
    return render(request, 'base/contact-us.html', context)

def service(request, pk_service):
    
    context = {}
    return render(request, 'base/service.html', context)

