
from django.contrib import admin
from django.urls import path
from users.views import userRegister,userLogin

urlpatterns = [
    path("register/",userRegister,name="register"),
    path("login/",userLogin,name="login"),
]