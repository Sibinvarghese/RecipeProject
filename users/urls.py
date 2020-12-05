
from django.contrib import admin
from django.urls import path
from users.views import userRegister,userLogin,userLogout,create_profile,edit_profile

urlpatterns = [
    path("register/",userRegister,name="register"),
    path("login/",userLogin,name="login"),
    path("logout/",userLogout,name="logout"),
    path("profile/",create_profile,name="profile"),
    path("edit/<int:pk>",edit_profile,name="editprofile"),

]