from django.db import models

class owner(models.Model):
    name= models.CharField(max_length=30)
    caption= models.TextField(max_length=200)
    gitLink= models.URLField()
    linkedinLink= models.URLField()
    personalImg= models.ImageField(upload_to="portfolioPage/static", default='https://www.google.com.eg/search?q=placeholder&hl=ar&authuser=0&tbm=isch&sxsrf=ALeKk01DOP5kqrJ08nTy8m1ePg9e3H4sKw%3A1618959191777&source=hp&biw=1829&bih=923&ei=V1t_YMuTLdKulwTkoYmQAg&oq=pla&gs_lcp=CgNpbWcQAxgAMgQIIxAnMgIIADICCAAyAggAMgUIABCxAzICCAAyAggAMgUIABCxAzICCAAyAggAOgcIIxDqAhAnUPwFWJMSYMwoaAFwAHgAgAF-iAG_A5IBAzAuNJgBAKABAaoBC2d3cy13aXotaW1nsAEK&sclient=img#imgrc=q1IkN7lSgxq0LM')

def __str__(self):
    return self.name
