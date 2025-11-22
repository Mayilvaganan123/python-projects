from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class QR_form(forms.Form):
    Rest=forms.CharField( required=True, max_length=100, label='RESTAURANT NAME', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Name'}))
    url=forms.URLField( required=True, max_length=200, label='URL', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter URL'}))

    
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
