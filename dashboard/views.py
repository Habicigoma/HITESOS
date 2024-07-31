from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail.message import EmailMessage
from django.conf import settings
from django.core import mail
from .models import Contact_us


# Create your views here.


def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def hightech_service(request):
    return render(request, 'hightech_service/hightech_service.html')

def latest_info(request):
    return render(request, 'latest_info/latest_info.html')

def market_service(request):
    return render(request, 'market_service/market_service.html')

def security_camera(request):
    return render(request, 'security_camera/security_camera.html')

def software_application_development(request):
    return render(request, 'software_aplication_development/software_application_development.html')


def website_development(request):
    return render(request, 'website_development/website_development.html')


def supply_hightech_equipment(request):
    return render(request, 'supply_hightech_equipment/supply_hightech_equipment.html')

def contact_us(request):
    if request.method=="POST":
        contact=Contact_us(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )
        contact.save()
        return HttpResponse("<h1>THANKS FOR CONTACT US. WE ARE AT YOUR SERVICE<h1>")

    return render(request, 'contact/contact_us.html')

