from django.shortcuts import render

from .models import Leader

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')  

def projects(request):
    return render(request, 'projects.html') 


def about(request):
    leader = Leader.objects.first()  # admin paneldagi birinchi lider
    return render(request, 'about.html', {'leader': leader})