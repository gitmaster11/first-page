from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import uuid

def validete_even(value):
    if len(value) != 14:
        raise  ValidationError("ValidationsError")
        params = {'value':value}

class BaseModel(models.Model):
    updated_to = models.DateTimeField(auto_now_add = True)
    created_to = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length = 150,verbose_name = "kategoriya_nomi")
    slug = models.SlugField(max_length = 160,verbose_name = "kategoriya_slugi")
    image_url = models.URLField(max_length = 300)
    is_active = models.BooleanField(default = True,verbose_name = "aktivmi")
    image = models.ImageField(upload_to = "images/cat_images")
   


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        db_table = "category"
        ordering = ['-created_to']


class Product(BaseModel):
    category = models.ForeignKey(Category,on_delete = models.PROTECT)
    name = models.CharField(max_length = 200,verbose_name = "mahsulot_nomi")
    price = models.FloatField(verbose_name = "mahsulot_narxi")
    stock = models.IntegerField(verbose_name = "mahsulot_soni")
    image = models.URLField(max_length = 300,verbose_name= 'Rasmi')
    



    class Meta:
        verbose_name = "Mahsulotlar"


    def __str__(self):
        return self.name


class PaymentChoice(models.Choices):
    PAYME = "Payme"
    UZCARD = "UzCard"
    HUMO = "Humo"
    CLICK = "Click"
    CASH = "Naqd pul"


class Order(BaseModel):
    first_name = models.CharField(max_length=255, verbose_name="Ism")
    last_name = models.CharField(max_length=255, verbose_name="Familiya")
    phone = models.CharField(max_length=255, verbose_name="Telefon")
    address = models.CharField(max_length=255, verbose_name="Manzil")
    city = models.CharField(max_length=255, verbose_name="Shahar")
    country = models.CharField(max_length=255, verbose_name="Davlat")
    zip_code = models.CharField(max_length=255, verbose_name="Indeks")
    total = models.FloatField(verbose_name="Umumiy summa")
    is_ordered = models.BooleanField(default=False, verbose_name="Buyurtma berildimi")
    is_paid = models.BooleanField(default=False, verbose_name="To'langanmi")
    payment_method = models.CharField(max_length=255, verbose_name="To'lov usuli", choices=PaymentChoice.choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi", null=True)
    jshshir = models.CharField(max_length = 14, validators = [validete_even],unique = True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Buyurtma"
        verbose_name_plural = "Buyurtmalar"
        db_table = "order"
        ordering = ["-created_to"]


class OrderProduct(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True, verbose_name='mahsulot nomi')
    quantity = models.SmallIntegerField(default=1, verbose_name='quantity')
    price = models.BigIntegerField(verbose_name='narxi', null=True)

    def save(self, *arg, **kwargs):
        if not self.pk:
            self.price = self.product.price
        super(OrderProduct, self).save(arg, kwargs)

    class Meta:
        verbose_name = 'Savatcha mahsulot'
        verbose_name_plural = 'Savatchadagi mahsulotlaar'




