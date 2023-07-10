from django.urls import path
from .views import Tasks, TaskDetail, CompleteTaskView, EditTaskView, DeleteTaskView, CreateTaskView

urlpatterns = [
    path('', Tasks.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/<int:pk>/complete/', CompleteTaskView.as_view(), name='complete_task'),
    path('task/<int:pk>/edit/', EditTaskView.as_view(), name='edit_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='confirm_delete'),
    path('create/', CreateTaskView.as_view(), name='create_task'),

]
