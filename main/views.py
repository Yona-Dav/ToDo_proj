from django.shortcuts import render, redirect
from .models import ToDo, Category
from .forms import ToDoForm
# Create your views here.

def add_task(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = ToDo.objects.create(**form.cleaned_data)
            return redirect('all_todo')
    if request.method == 'GET':
        form = ToDoForm()
    return render(request, 'add_todo.html', {'form':form})

def all_todos(request):
    return render(request, 'todos.html', {'todo': ToDo.objects.all()})
