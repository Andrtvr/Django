from django.conf.urls import url
from django.db import models


from . import views
'''
urlpatterns = [
    url(r'^$', views.new_quest, name='new_quest'),
    url(r'^question/(?P<pk>\d+)/', views.question, name='question_detail'),
    #url(r'^/popular$', views.popular, name='popular'),


]
'''
urlpatterns = [
    url(r'^$', views.new_quest, name='new_quest'),
    url(r'^question/(?P<pk>\d+)/', views.question, name='question_detail'),
    url(r'^popular/', views.popular, name='popular'),
   # url(r'^ask/', question_ask, name='question_ask'),
    #url(r'^answer/', question_answer, name='question_answer'),
    #url(r'^signup/', user_signup, name='signup'),
    #url(r'^login/', user_login, name='login'),
    #url(r'^logout/', user_logout, name='logout'),
    #url(r'^new/', test, name='new'),
]
