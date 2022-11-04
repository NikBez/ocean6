from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Title</h1><p>subtittle</p>')

def catalog(request):
    return HttpResponse('Catalog')


