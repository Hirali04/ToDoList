from django.shortcuts import render,redirect
from .models import *
from .forms import TaskForm, CreateUserForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout



def list(request):
     if request.user.is_authenticated:
        tasks = Task.objects.filter(created_by=request.user)
        return render(request, 'list.html', {'tasks': tasks})
     else:
        return redirect('signin')

def details(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'details.html', {'task': task})

def create(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.created_by = request.user
                task.save()
                return redirect('list')
        else:
            form = TaskForm()
        return render(request, 'form.html', {'form': form})
    else:
        return redirect('signin')

def update(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'form.html', {'form': form})

def delete(request, pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('list')
    return render(request, 'confirm.html', {'task': task})

###

def signup(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
             user = form.save()
             login(request, user)
             return redirect('list')
    else:
        form = CreateUserForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('signin')