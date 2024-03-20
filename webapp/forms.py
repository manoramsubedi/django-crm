from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms 
from django.forms.widgets import PasswordInput, TextInput

from .models import Record

class RegisterForm(UserCreationForm):
    class Meta:
        model = User   #build-in model
        fields = ['username', 'password1','password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    
#add record
class AddRecordForm(forms.ModelForm):
     class Meta:
        model = Record   #model from models.py
        fields = ['first_name', 'last_name','email','phone','address','city','country']


#update record:
class UpdateRecordForm(forms.ModelForm):
     class Meta:
        model = Record #model from models.py
        fields = ['first_name', 'last_name','email','phone','address','city','country']







