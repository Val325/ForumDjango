from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import textData, SubPost

class UserForm(forms.ModelForm):
    textdata = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "cols": "40"}))
    image = forms.ImageField(required=False)
    class Meta:
        model = textData
        fields = ("textdata", "image")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    
class SubPostForm(forms.ModelForm):
    textdata = forms.CharField(widget=forms.Textarea(attrs={"rows":"5", "cols": "40"}))
    image = forms.ImageField(required=False)
    class Meta:
        model = SubPost
        fields = ('textdata','image')
    

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2'] 