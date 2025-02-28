from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class Registro(UserCreationForm):
    first_name = forms.CharField(max_length=30, help_text="Ingrese su nombre")
    last_name = forms.CharField(max_length=30, help_text="Ingrese su apellido")
    email = forms.EmailField(max_length=100, help_text="Ingrese su correo")
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields =  ("username", "first_name", "last_name", "email", "password1", "password2")