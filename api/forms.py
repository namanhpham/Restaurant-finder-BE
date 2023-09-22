from django import forms
import re 
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegisterForm(forms.Form):
    username = forms.CharField(label = 'Username', max_length=30)
    email = forms.EmailField(label = 'Email')
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label = 'Confirm Password', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Password do not match') #if password1 and password2 are not equal, then raise an error
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Username is already taken.')
    def save(self):
        User.objects.create_user(username=self.cleaned_data.get('username'), email=self.cleaned_data.get('email'), password=self.cleaned_data.get('password1'))