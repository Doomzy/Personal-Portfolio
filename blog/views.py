from django.shortcuts import render , get_object_or_404
from portfolioPage.models import owner
from .models import article


def articles(request):
    ownerInfo= owner.objects.get()
    allArticles= article.objects.all()
    return render(request, "articles.html", {"owner":ownerInfo , "articles": allArticles})

def articlePage(request, article_id):
    articleInfo= article.objects.get(id= article_id)
    return render(request, "article.html", {"article": articleInfo})
