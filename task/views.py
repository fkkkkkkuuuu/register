from django.shortcuts import render, get_object_or_404
from .models import Task



def task_index(request):
    tasks = Task.objects.all()
    data = {'title': 'Main page'}
    return render(request, 'task/task_index.html', {'title': 'Main page', 'tasks': tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task/task_detail.html', {'task': task})