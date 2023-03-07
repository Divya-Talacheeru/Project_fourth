from django.shortcuts import render
from django.http import HttpResponse
def divya(request):
    return HttpResponse('<h1><marquee>my name is divya</marquee></h1>')

# Create your views here.
