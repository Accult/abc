from django.urls import path
from .views import Tasks, TaskDetail, CompleteTaskView

urlpatterns=[
    path('', Tasks.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/<int:pk>/complete/', CompleteTaskView.as_view(), name='complete_task'),

]