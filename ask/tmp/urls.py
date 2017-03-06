from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.tmp_a, name='tmp_a'),
    #url(r'^(?P<page>[0-9]+)\$', views.tmp, name='tmp_a'),
]
