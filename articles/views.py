from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def article(request):
    return render(request, 'article/article.html')
    # return HttpResponse('aws');