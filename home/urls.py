from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_other'),
    path('about-us', views.about, name='about'),

]
