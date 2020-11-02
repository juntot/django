from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
# Create your views here.
def article(request):
    # ORM
    article = Articles.objects.all()

    # RAW SQL
    # article  = Articles.objects.raw('select * from articles_articles')

    return render(request, 'article/article.html', {'articles': article})
    # return HttpResponse('aws')

def article_detail(request, slugs):
    article = Articles.objects.get(slug=slugs)
    # return HttpResponse(slug)
    return render(request, 'article/article_detail.html', { 'articles': article })