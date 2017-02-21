from django.shortcuts import render
from django.http import HttpResponse 
def signup(request, *args, **kwargs):
    return HttpResponse('This is signup')


