from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import  Submit
from pages.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Select, EmailInput, NumberInput
from crispy_forms.layout import Layout, Field

class ctreateuserform(UserCreationForm):
    class Meta:
        model = User
        fields = ['FirstName','is_superuser','lastName', 'nationality', 'phone_number', 'password1', 'password2', 'email', 'gender','BIrthDate']
       

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)        