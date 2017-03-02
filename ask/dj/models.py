from __future__ import unicode_literals

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    Choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



'''
class Author(models.Model):
    rating = models.IntegerField()
    name = models.CharField(max_length=50)

class Article():
    author = models.ForeignKey(Author)
    text = models.TextField()
'''
