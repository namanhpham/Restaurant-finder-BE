from django.shortcuts import render
from rest_framework import generics, status
from .serializers import FavoriteRestaurantSerializer
from .models import FavoriteRestaurant
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse
# Create your views here.


def index(request, *args, **kwargs):
    return HttpResponse("Hello, world. You're at the API index.")

class FavoriteRestaurantView(generics.ListAPIView):
    queryset = FavoriteRestaurant.objects.all()
    serializer_class = FavoriteRestaurantSerializer