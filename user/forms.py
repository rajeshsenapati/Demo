from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import PostModel


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = "__all__"

