from django.contrib import admin
from django.urls import path, include
from CRUD import views

urlpatterns = [
    path('',views.index,name="home"),
    path('add',views.add,name="add"),
    path('update/<str:id>',views.update,name="update"),
    path('delete/<str:id>',views.delete,name="delete"),
]
