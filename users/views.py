from django.shortcuts import render,redirect
from users.forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout
from users.forms import ProfileCreateForm
from .models import Profile
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
    # form=UserLoginForm()
    # context={}
    # context["form"]=form
    # if request.method=="POST":
    #     form=UserLoginForm(request.POST)
    #     # print("enter the if block")
    #     if form.is_valid():
            # print("enter the valid function")
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                # print("user okay")
                login(request,user)
                return redirect("allrecipes")
                # return render(request, "users/home.html")

            else:
                return render(request, "users/signin.html")
        # else:
        #     # print("not okay if blocks")
        #     # context["form"]=form
    # return render(request,"users/signin.html")

def userLogout(request):
    logout(request)
    return redirect("login")

def create_profile(request):
    form=ProfileCreateForm(initial={"user":request.user})
    context={}
    context["form"]=form
    updates=Profile.objects.filter(user=request.user)
    context["updates"]=updates
    if request.method=="POST":
        form=ProfileCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return render(request,"users/home.html")
        else:
            context["form"]=form
    return render(request,"users/createprofile.html",context)


def edit_profile(request,pk):
    id=Profile.objects.get(id=pk)
    form=ProfileCreateForm(initial={"user":request.user},instance=id)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProfileCreateForm(instance=id,data=request.POST,files=request.FILES)
        if form.is_valid():
            # print("save")
            form.save()
            return redirect("profile")
        else:
            context["form"]=form
            # print("not save")
    return render(request,"users/editprofile.html",context)


def view_profile(request):
    user=Profile.objects.get(user=request.user)
    context = {}
    context["user"] = user
    return render(request,"users/viewprofile.html",context)
