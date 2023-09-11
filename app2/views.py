from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first2(request):
    return render (request, 'first2.html')

def second2(request):
    return render (request, 'second2.html')

def third2(request):
    return HttpResponse('<h1>Thor</h1')