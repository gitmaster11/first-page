from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("",loginview,name = "log"),
    path("reg/",registration, name= "reg"),
    path("main/",all_user,name = "main"),
    path("del/",delete_page,name = "del")]
