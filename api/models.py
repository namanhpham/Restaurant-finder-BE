from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FavoriteRestaurant(models.Model):
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)