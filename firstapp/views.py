from django.shortcuts import render
from django.http import HttpResponse
from .models import Students

def index(request):
    students = Students.objects.all().values()

    return render(request, 'firstapp/main.html',{
        "students": students,
    })

def about(request):
    today = today()
    return render(request, "firstapp/index.html",)