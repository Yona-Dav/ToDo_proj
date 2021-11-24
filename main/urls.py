from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all_todos, name='all_todo'),
    path('add/', views.add_task, name='add_task')
]
