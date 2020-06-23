from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.models import User # default user model, if you don't use the custom user model above
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
