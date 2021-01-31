from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('login' , login_attempt , name="login_attempt"),
    path('register' , register_attempt , name="register_attempt")
]
