from django.urls import path
from .views import *

urlpatterns = [
    path("",main_view,name  = "main"),
    path("contact/",contact_view,name = "contact"),
    path("single_view/",single_view,name = "single"),
    path("single_page/<str:str>/<slug:slug>/", single_view_about,name = "single_view")
]