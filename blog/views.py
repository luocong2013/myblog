from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def hello(request):
    return HttpResponse("Hello World")


def index(request):
    return render(request, 'blog/index.html', {'hello': 'hello, hello, hello'})


def index_models(request):
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/index_models.html', {'article': article})
