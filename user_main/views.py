from django.shortcuts import render

from .models import UserTask
from django.views.generic import DetailView


def user_index(request):
    tasks = UserTask.objects.all()
    data = {'title': 'Main page'}
    return render(request, 'user_main/user_index.html', {'title': 'Main page', 'tasks': tasks})



def user_about(request):
    return render(request, 'user_main/user_about.html')
