from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    yet_to_start_tasks = Task.objects.filter(status='not_started')
    in_progress_tasks = Task.objects.filter(status='in_progress')
    completed_tasks = Task.objects.filter(status='completed')
    return render(request, 'tasks/task_list.html', {
        'yet_to_start_tasks': yet_to_start_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
    })

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def start_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'in_progress'
    task.in_progress = True
    task.save()
    return redirect('task_list')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = 'completed'
    task.in_progress = False
    task.save()
    return redirect('task_list')


# Create your views here.
