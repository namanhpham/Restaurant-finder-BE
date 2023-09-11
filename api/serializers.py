from rest_framework import serializers
from .models import FavoriteRestaurant

class FavoriteRestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRestaurant
        fields = ['id','user_id', 'name', 'address', 'created_at']

class FavoriteRestaurantSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = FavoriteRestaurant
        fields = ['user_id', 'name', 'address', 'created_at']