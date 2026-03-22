from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
 path("", views.index, name='index'),
    path("furm.html/", views.register, name='register'),
    path("form.html/", views.administration, name='administration')   
]
