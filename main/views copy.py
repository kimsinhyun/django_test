from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # items = ls.item_set.get(id=1)
    return render(response, "main/list.html", {'ls': ls})


def home(response):
    return render(response, "main/home.html", {})


def creata(response):
    return render(response, "main/create.html", {})
