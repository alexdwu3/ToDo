from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

# returns an http response
def index(requests): 
    tasks = Task.objects.all() # gets tasks from models.py
    form = TaskForm()

    if requests.method == "POST":
        form = TaskForm(requests.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'tasks':tasks, 'form': form}
    return render(requests, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance = task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'tasks/updateTask.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == "POST":
        item.delete()
        return redirect('/')
    context = {'item':item}
    return render(request, 'tasks/delete.html', context)