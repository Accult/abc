from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from django.views.generic.detail import DetailView

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class Tasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class CompleteTaskView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = Task.objects.get(pk=pk)

        task.complete = not task.complete
        task.save()

        return redirect('task', pk=pk)


class EditTaskView(LoginRequiredMixin, View):


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


class DeleteTaskView(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'base/confirm_delete.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('tasks')


class CreateTaskView(LoginRequiredMixin, View):
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

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTaskView, self).form_valid(form)
