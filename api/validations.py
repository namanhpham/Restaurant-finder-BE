from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

def validate_data(data):
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    if not email or User.objects.filter(email=email).exists():
        raise ValidationError({'email': 'Email is invalid or already exists.'})
    if not username or User.objects.filter(username=username).exists():
        raise ValidationError({'username': 'Username is invalid or already exists.'})
    if not password:
        raise ValidationError({'password': 'Please enter password.'})

def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('an email is needed')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('choose another username')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('a password is needed')
    return True
