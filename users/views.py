from django.shortcuts import render,redirect
from users.forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login
# Create your views here.


def userRegister(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # print("hello saved")
            return redirect("login")
        else:
            context["form"]=form
            return render(request,"users/register.html",context)
    return render(request,"users/register.html",context)


#just a try

def userLogin(request):
    form=UserLoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserLoginForm(request.POST)
        # print("enter the if block")
        if form.is_valid():
            # print("enter the valid function")
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                # print("user okay")
                login(request,user)
                return render(request, "users/home.html")

            else:
                return render(request, "users/login.html", context)
        else:
            # print("not okay if blocks")
            context["form"]=form
    return render(request,"users/login.html",context)