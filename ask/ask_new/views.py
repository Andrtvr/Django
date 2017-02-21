from django.shortcuts import render
from django.http import HttpResponse 
def ask_new(request, *args, **kwargs):
    return HttpResponse('This is NEW')

# Create your views here.
