from django.urls import path
from .views import *

urlpatterns = [
    path("",mainview,name = 'main'),
    path("add_product/",add_product,name = 'add'),
    path("update_product/<int:pk>/",update_product,name = 'update_product'),
    path("add_category/",add_category,name = "add_category"),
    path("pay_book/",pay_book,name = 'pay_book'),
]