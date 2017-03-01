from __future__ import unicode_literals
from django.db import models, connection


class Users(models.Model):
     login = models.CharField(max_length=20)
     Name = models.TextField()




class Question(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=200)
    added_at = models.DateTimeField('Date published')
    rating = models.IntegerField('Rating')
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    likes = models.TextField('Likes')


class Answer(models.Model):
     text = models.CharField(max_length=200)
     added_at = models.DateTimeField('Date published')
     question = models.TextField()
     author = models.TextField()


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

