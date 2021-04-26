from django.urls import path,include
from . import views

app_name= 'blog'

urlpatterns = [
    path('', views.articles, name="articles"),
    # path('/post', views.article, name="article"),
]