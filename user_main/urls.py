from django.urls import path
from . import views


urlpatterns = [
    path('jipdv', views.user_index, name='user_main'),
    path('about-us', views.user_about, name='user_about'),
    path('index/id:task_id', views.user_index, name='user_index')
   ]