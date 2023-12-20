from django.shortcuts import render
from .models import EventModel


def news_page(request):
    event = EventModel.objects.all()
    return render(request, 'news/news_home.html', {'event': event})
