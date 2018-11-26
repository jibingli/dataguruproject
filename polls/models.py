from django.db import models


# Create your models here.

# 问题表
class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text


# 选项
class Choice(models.Model):
    choice_text = models.CharField(max_length=500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# 登录
class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.username