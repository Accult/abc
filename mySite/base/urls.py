from django.urls import path
from .views import Tasks, TaskDetail, CompleteTaskView, EditTaskView, DeleteTaskView, CreateTaskView, CustomLoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', Tasks.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task/<int:pk>/complete/', CompleteTaskView.as_view(), name='complete_task'),
    path('task/<int:pk>/edit/', EditTaskView.as_view(), name='edit_task'),
    path('task/<int:pk>/delete/', DeleteTaskView.as_view(), name='confirm_delete'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

]
