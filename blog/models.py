from django.db import models

class article(models.Model):
    title= models.CharField(max_length=200)
    date= models.DateTimeField(auto_now_add=True, blank=False)
    content= models.TextField(blank=False)
    
    def snppet(self):
        return self.content[:400]

    def __str__(self):
        return self.title
