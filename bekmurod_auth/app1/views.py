
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login
import json
from django.http import JsonResponse ,HttpResponse  




# Create your views here.
def loginview(request):
    if request.method == "POST":
        try:
            name = request.POST.get("username")
            password = request.POST.get("password")
            user = IntroModel.objects.get(name = name,password = password)
            return redirect('main')  
        except IntroModel.DoesNotExist:
            print("mavjud emas") 
            return redirect("reg")

    else:
        return render(request,"index.html")
    
        
        # form = CustomLoginForm(request,data = request.POST)
        # if form.is_valid():
        #     username = form.cleaned_data.get("name")
        #     password = form.cleaned_data.get("password")
        #     user = authenticate(username = username,password = password)
        #     if user is not None:
        #         # login(request,user)
        #         # return redirect("main")
        #     else:
        #         return redirect("reg")
    



def registration(request):

    if request.method == 'POST':
        data = request.POST
        form = IntroModelForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('main')  # Redirect to a home or success page
            
    form  = IntroModelForm()
    return render(request,"reg.html",{"data":form})


   # Intromodel.objects.create ( name = data.get("username"),
        # email = data.get("email"),
        # password = data.get("password"))
        # return redirect("main")


def all_user(request):
    data = IntroModel.objects.all()
    return render(request,"main.html",{"data":data})



def delete_page(request):

    if request.method == "POST":
        username = request.POST.get("username")   
        password = request.POST.get("password")
        email = request.POST.get("email")
        users = IntroModel.objects.filter(name = username,email = email,password = password)
        count = users.count() 
        if count>0:
            users.delete()
            return redirect("main")
        else:
            print("Mavjud emas")
            return redirect("del")
    return render(request,"delete.html")