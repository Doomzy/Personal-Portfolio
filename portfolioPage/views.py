from django.shortcuts import render
from .models import owner,project

def mainPage(request):
    projects= project.objects.all()
    ownerInfo= owner.objects.get()
    return render(request, "portfolio.html" ,{"owner":ownerInfo , "projects":projects})
