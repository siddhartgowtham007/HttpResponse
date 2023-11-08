from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def firstone(request):
    return HttpResponse ('have lots of fun')

def secondone(request):
    return HttpResponse ('earn mor money')