from dataclasses import field, fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from Flower.models import User
from .models import Producto

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

