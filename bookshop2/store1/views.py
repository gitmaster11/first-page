from django.shortcuts import render,redirect,Http404
from .models import *
from .forms import ProductModelForm,CategoryFormModel,OrderChoiceForm
# Create your views here.


def mainview(request):
    products = Product.objects.all().select_related('category')
    return render(request,"main.html",{"products":products})



def add_product(request):
#FrontEnd dan qaytayotgan malumot
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        print(request.POST, form.is_valid(), form.errors, form.data)
#FrondEnd ga ketayotgan malumot
    form  = ProductModelForm()
    return render(request,'add_product.html',{'form':form})



def update_product(request,pk):
#FrondEnddan qaytayotgan malumot
    product = Product.objects.filter(id = pk).first()
    if not product:
        return Http404
    if request.method == "POST":
        form = ProductModelForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('main')
#FrondEndga ketayotgan malumot

    form = ProductModelForm(instance = product)
    return render(request,'update_detail.html',{"form":form})

def add_category(request):
    #qaytayotgan malumot

    if request.method == "POST":
        form = CategoryFormModel(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
            
    #frondendga ketayotgan malumot 
    form = CategoryFormModel()
    return render(request,'add_category.html',{"form":form})

def pay_book(request):
    if request.method == 'POST':
        form = OrderChoiceForm(request.POST)
        if form.is_valid():
            # print(request.POST, form.is_valid(), form.errors, form.data)
            print(form.data)
            return redirect('main')




    form = OrderChoiceForm()
    return render(request,'pay.html',{"form":form})
    

    
