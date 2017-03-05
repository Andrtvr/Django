from django.conf.urls import url
from django.db import models


from . import views

urlpatterns = [
    #url(r'^$', views.qa, name='qa'),
    url(r'^(?P<page>\d+)$', views.qa, name='new_quest')
]
