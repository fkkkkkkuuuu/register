from django.urls import path, include
from register.views import Register
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),

]