from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def dj(request):
    template=loader.get_template('dj/tmp.html')
    return HttpResponse(template.render())
