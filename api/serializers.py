from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ValidationError

from .models import FavoriteRestaurant

UserModel = User

class FavoriteRestaurantSerializerGet(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRestaurant
        fields = ['id','user_id', 'name', 'address', 'created_at']

class FavoriteRestaurantSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRestaurant
        fields = ['user_id', 'name', 'address', 'created_at']

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password']
    def create(self, cleaned_data):
        user_obj = UserModel.objects.create_user(
                username = cleaned_data['username'],
                email = cleaned_data['email'],
                password = cleaned_data['password']
        )
        user_obj.save()
        return user_obj

class UserLoginSerializer(serializers.Serializer):
	username = serializers.CharField()
	password = serializers.CharField()
	##
	def check_user(self, clean_data):
        # authenticate user with username and password is a built-in function
		user = authenticate(username=clean_data['username'], password=clean_data['password'])
		if not user:
			raise ValidationError('user or password not found')
		return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['username', 'email']
