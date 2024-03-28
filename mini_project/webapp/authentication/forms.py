from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']