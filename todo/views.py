from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Todo
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator
import json

# Create your views here.
def index(request):

    todos = Todo.objects.all().order_by("id").reverse()

    todos = list(todos)

    paginator = Paginator(todos, 4)

    pgnum = request.GET.get('page')

    posts_of_the_page = paginator.get_page(pgnum)

    return render(request, "todo/index.html", {
        "todos": todos,
        "posts_of_the_page": posts_of_the_page
    })

def remove(request, item_id):

    item = Todo.objects.get(pk=item_id)

    item.delete()

    messages.info(request, "item removed !!!")

    return HttpResponseRedirect('/')

def create(request):

    if request.method == "POST":

        todos = Todo.objects.all()

        todos = list(todos)

        data = request.POST

        data = data.dict()

        title = data["text"]

        content = data["content"]

        lis = []

        for i in todos:

            if i.title == title:

                lis.append(i)

        print(lis)

        if lis != []:

            return render(request, "todo/exists.html")

        elif lis == []:

            bruh = Todo(title=title, details=content)

            bruh.save()

            return HttpResponseRedirect(f"notes/{title}")

    else:

        return render(request, "todo/create.html")

def form(request):

    if request.method == "POST":

        data = request.POST

        data = data.dict()

        data1 = data["q"]

        todo = Todo.objects.all()

        todo = list(todo)

        print(todo)

        lis = []

        for i in todo:

            var = f"{i}"

            if data1 in var:

                lis.append(i)

        print(lis)

        if lis != []:

            return render(request, "todo/result.html", {
                "datum": lis
            })

        elif lis == []:

            return render(request, "todo/apology.html")

def filename(request, filename):

    todo = Todo.objects.all()

    todo = list(todo)

    name = filename

    bruh = Todo.objects.get(title=name)

    bruh2 = bruh.details

    bruh3 = bruh.id

    bruh4 = bruh.date

    lis = []

    for i in todo:

        ooo = f"{i}"

        if name == ooo:

            lis.append(i)

    if lis != []:

        return render(request, "todo/filename.html", {
            "title": name, 
            "content": bruh2,
            "todos": bruh,
            "date": bruh4,
            "id": bruh3
        })

def edit(request, postId):

    if request.method == "POST":

        data  = json.loads(request.body)

        edit_post = Todo.objects.get(pk=postId) 

        edit_post.details = data["content"]

        edit_post.save()

        print(data["content"])

        return JsonResponse({"data": data["content"]})