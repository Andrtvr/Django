from __future__ import unicode_literals
from django.db import models, connection
from django.contrib.auth.models import User, UserManager

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

class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    added_at = models.DateTimeField(blank=True, auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    likes = models.ManyToManyField(User, related_name='Likes')
    questionMa = QuestionManager()

class Answer(models.Model):
     text = models.TextField(max_length=200)
     added_at = models.DateTimeField('Date published')
     question = models.ForeignKey(Question)
     author = models.ForeignKey(User)

