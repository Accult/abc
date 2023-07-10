from django.shortcuts import render, redirect, get_object_or_404
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
        task = Task.objects.get(pk=pk)

        task.complete = True
        task.save()

        return redirect('task', pk=pk)


class EditTaskView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk=pk)
        return render(request, 'base/edit_task.html', {'task': task})

    def post(self, request, pk):
        task = Task.objects.get(pk=pk)

        title = request.POST.get('title')
        complete = request.POST.get('complete')
        description = request.POST.get('description')

        task.title = title
        task.complete = complete == 'on'
        task.description = description

        task.save()

        return redirect('tasks')


class DeleteTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'base/confirm_delete.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('tasks')


class CreateTaskView(View):
    def get(self, request):
        return render(request, 'base/create_task.html')

    def post(self, request):
        title = request.POST.get('title')
        complete = request.POST.get('complete', False) == 'on'
        description = request.POST.get('description')

        task = Task.objects.create(
            title=title,
            description=description,
            complete=complete
        )

        return redirect('tasks')
