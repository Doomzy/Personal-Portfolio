from django.urls import path
from . import views

app_name= "portfolioPage"

urlpatterns =[
    path('', views.mainPage, name="portfolio")
]

