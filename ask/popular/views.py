from django.shortcuts import render
from django.http import HttpResponse 
def popular(request, *args, **kwargs):
    return HttpResponse('This is super popular page')

# Create your views here.
