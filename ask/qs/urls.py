from django.conf.urls import url

from . import views

urlpatterns = [
   # url(r'^qs/(?P<id>[0-9])/$', views.qs_t, name='qs_t'),
    url(r'^$', views.qs_t, name='qs_t'),
    #url(r'^qs/(?P<id>[0-9])/$', views.qs_t, name='qs_t')
]
