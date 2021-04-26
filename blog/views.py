from django.shortcuts import render
from portfolioPage.models import owner


def articles(request):
    ownerInfo= owner.objects.get()
    return render(request, "articles.html", {"owner":ownerInfo})

def article(request):
    return render(request, "article.html")
