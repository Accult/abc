from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

class Tasks(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task_list.html'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'



