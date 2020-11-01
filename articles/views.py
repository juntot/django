from django.shortcuts import render
from django.http import HttpResponse
from .models import Articles
# Create your views here.
def article(request):
    article = Articles.objects.all()
    return render(request, 'article/article.html', {'articles': article})
    # return HttpResponse('aws');