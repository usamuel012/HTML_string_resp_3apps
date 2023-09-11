from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def first3 (request):
    return render(request, 'first3.html')

def second3(request):
    return render (request, 'second.html')

def third3 (request):
    return HttpResponse ('<h1>A-Train</h1>')