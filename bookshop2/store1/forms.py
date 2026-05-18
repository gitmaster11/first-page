from django import forms
from .models import Category,Product,PaymentChoice,Order



class ProductModelForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category','name','price','stock','image']

    def clean_image(self):  
        image = self.cleaned_data['image'].split(".")[-1]
        if image not in ['jpg','JPG','PNG','png']:
            raise forms.ValidationError("Rasm noto'gri formatda")
        return self.cleaned_data['image']

    def clean_stock(self):
        if self.cleaned_data['stock']<0:
            raise forms.ValidationError("Mahsulot soni manfiy bo'la olmaydi")
        return self.cleaned_data['stock']


class CategoryFormModel(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','slug','image_url',"is_active"]
    def clean_image(self):
        image = self.cleaned_data['image'].split(".")[-1]
        if image not in ['jpg','JPG','PNG','png']:
            raise forms.ValidationError("Rasm noto'gri formatda")
        return self.cleaned_data['image']


class OrderChoiceForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['phone','first_name','address','payment_method']
       
        