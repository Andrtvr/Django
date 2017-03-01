from __future__ import unicode_literals
from django.db import models, connection
from django.contrib.auth.models import User, UserManager


class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    likes = models.ManyToManyField(User, related_name='Likes')

class Answer(models.Model):
     text = models.CharField(max_length=200)
     added_at = models.DateTimeField('Date published')
     question = models.TextField()
     author = models.TextField()
'''
class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    inviter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Likes_invites')
    invite_reason = models.TextField()
'''

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

