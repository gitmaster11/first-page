from django import forms

from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class IntroModelForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = IntroModel
        fields = "__all__"

      
    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        if IntroModel.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")

        return cleaned_data



# class CustomLoginForm(AuthenticationForm):
#     name = forms.CharField(label = "Name",widget = forms.TextInput(attrs = {"class":"form-control"}))
#     password = forms.CharField(label = "Password",widget = forms.PasswordInput(attrs = {"class":"form-control"}))