from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
# Create your views here.


def index(response, id):
    ls = Item.objects.get(id_test=id)
    # items = ls.item_set.get(id=1)
    return render(response, "main/list.html", {'ls': ls})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        print("POST")
        form = CreateNewList(response.POST)
        print(type(form))

        if form.is_valid():
            n = form.cleaned_data['name']
            print(n)
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect('/%i' % t.id)
    else:
        print("GET")
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})


def signUp(response):
    if response.method == "POST":
        # print(response.POST)
        print(response.POST.get("userEmail"))
    return render(response, "main/signUp.html", {})
