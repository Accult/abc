from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views import View
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



class CompleteTaskView(View):
    def post(self, request, pk):
        # Retrieve the task object
        task = Task.objects.get(pk=pk)

        # Update the task's completion status
        task.complete = True
        task.save()

        # Redirect back to the task detail page
        return redirect('task', pk=pk)









