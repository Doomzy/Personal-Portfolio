from django.db import models

class owner(models.Model):
    name= models.CharField(max_length=30)
    caption= models.TextField(max_length=200)
    gitLink= models.URLField()
    linkedinLink= models.URLField()
    personalImg= models.URLField()

class project(models.Model):
    name= models.CharField(max_length=50)
    prLink= models.URLField()
    info= models.TextField(max_length=200)
    prImage= models.URLField()
    
def __str__(self):
    return self.name
