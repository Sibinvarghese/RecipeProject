from django.shortcuts import render,redirect
from recipes.forms import CreatedRecipeForm
from recipes.models import Recipe
# Create your views here.

def create_recipe(request):
    form=CreatedRecipeForm(initial={"created_by":request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreatedRecipeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # print("save data")
            return redirect("viewrecipes")
        else:
            context["form"]=form
            print("not saved")

    return render(request,"recipes/createrecipe.html",context)

def view_recipes(request):
    recipe=Recipe.objects.filter(created_by=request.user)
    context={}
    context["recipe"]=recipe
    return render(request,"recipes/myrecipes.html",context)

def edit_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    form=CreatedRecipeForm(instance=recipe)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreatedRecipeForm(instance=recipe,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("viewrecipes")
        else:
            context["form"]=form
            return render(request, "recipes/editrecipe.html", context)

    return render(request,"recipes/editrecipe.html",context)

def view_my_recipes(request,id):
    recipe=Recipe.objects.get(id=id)
    # print(id)
    context={}
    context["recipe"]=recipe
    return render(request,"recipes/recipeview.html",context)

def delete_recipe(request,id):
    Recipe.objects.get(id=id).delete()
    return redirect("viewrecipes")

def all_recipe(request):
    recipe=Recipe.objects.all()
    context={}
    context["form"]=recipe
    return render(request,"recipes/homepage.html",context)