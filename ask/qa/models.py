from __future__ import unicode_literals
from django.db import models, connection
from django.contrib.auth.models import User, UserManager

class Likes(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    added_at = models.DateTimeField('Date published')
    rating = models.IntegerField('Rating')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Likes)
   # likes = models.ManyToManyField(User, through='Likes', through_fields=('user','question'))

class Answer(models.Model):
     text = models.CharField(max_length=200)
     added_at = models.DateTimeField('Date published')
     question = models.TextField()
     author = models.TextField()
"""
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    inviter = models.ForeignKey(User,on_delete=models.CASCADE)
    invite_reason = models.CharField
"""

class QuestionManager(models.Manager):
    def new(self):
        cursor = connection.cursor()
        cursor.execute(""" SELECT title,text FROM qa_question ORDER BY id DESC LIMIT 3 """)
        result_list = []
        for i in cursor.fetchall():
            c = result_list.append(i)
        return result_list

    def popular(self):
        cursor = connection.cursor()
        cursor.execute(""" SELECT title, text FROM qa_question ORDER BY rating""")
        result_list = []
        for i in cursor.fetchall():
            c = result_list.append(i)
        return result_list

