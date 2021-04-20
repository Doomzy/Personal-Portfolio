from django.urls import path
from . import views

name= "portfolioPage"

urlpatterns =[
    path('', views.mainPage)
]