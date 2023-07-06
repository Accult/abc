from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task

class Tasks(ListView):
    model = Task
    context_object_name = 'Tasks'
    template_name = 'base/task_list.html'


