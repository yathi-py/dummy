from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['email', 'username', 'password1', 'password2']