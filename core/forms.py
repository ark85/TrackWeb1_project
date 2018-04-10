from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = 'username', 'email', 'password',
