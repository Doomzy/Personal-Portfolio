from django.shortcuts import render
from .models import owner

def mainPage(request):
    ownerInfo= owner.objects.get()
    return render(request, "portfolio.html" ,{"owner":ownerInfo})
