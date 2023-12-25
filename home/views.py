from django.shortcuts import render
from .models import StringRun


def index(request):

    string_ = StringRun.objects.all()

    return render(request, 'main/index.html', {'string_': string_})


def about(request):
    return render(request, 'main/about.html')

