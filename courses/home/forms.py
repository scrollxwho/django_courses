from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):

    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')