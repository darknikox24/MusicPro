from django import forms
from .models import Insumos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class InsumosForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=120, required = True)
    precio = forms.IntegerField(min_value=1, required = True)
    imagen = forms.ImageField(required = False)
    cantidad = forms.IntegerField(min_value=0, required = True)

    class Meta:
        model = Insumos
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name","email","password1","password2"]