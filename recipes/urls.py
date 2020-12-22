
from django.contrib import admin
from django.urls import path
from recipes.views import create_recipe,view_recipes,edit_recipe,view_my_recipes,delete_recipe,all_recipe

urlpatterns = [

    path("create/",create_recipe,name="createrecipes"),
    path("listview/",view_recipes,name="viewrecipes"),
    path("edit/<int:id>",edit_recipe,name="editrecipe"),
    path("view/<int:id>",view_my_recipes,name="view"),
    path("delete/<int:id>",delete_recipe,name="delete"),
    path("Home",all_recipe,name="allrecipes"),


]