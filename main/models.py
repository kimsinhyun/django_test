from pyexpat import model
from django.db import models

# Create your models here.


class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class People(models.Model):
    user_name = models.CharField(max_length=200, verbose_name="사용자 이름")
    email = models.EmailField(max_length=20, verbose_name="사용자 이메일")


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList,  on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
