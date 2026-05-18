from django.shortcuts import render
from .models import *
def main_view(request):
    football = Sport_New.objects.filter(turi = "matching")
    trasfer = Sport_New.objects.filter(turi = "transfer")
    main = Sport_New.objects.filter(turi = "main")
    context = {
        "sport_1":football,
        "sport_2":trasfer,
        "sport_3":main
    }
    return render(request,"index.html",context)
 

def contact_view(request):
    return  render(request,"contact.html",{})


def single_view(request):
    return render(request,"single-page.html",{})


def single_view_about(request,slug,str):
    news = Sport_New.objects.get(slug = slug,turi = str)
    cat_news = Sport_New.objects.filter(turi = str) 
    context = {
        "news":news,
        "cat_news":cat_news,
    }
    return render(request,"single-page.html",context)