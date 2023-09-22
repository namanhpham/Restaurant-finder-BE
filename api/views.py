from django.shortcuts import render
from rest_framework import generics, status, permissions 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from .validations import validate_data, validate_username, validate_password

from .forms import RegisterForm
from .serializers import FavoriteRestaurantSerializerGet, UserLoginSerializer, UserRegisterSerializer, UserSerializer
from .models import FavoriteRestaurant
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import HttpResponse
# Create your views here.


def index(request, *args, **kwargs):
    return HttpResponse("Hello, world. You're at the API index.")

class FavoriteRestaurantView(generics.ListAPIView):
    queryset = FavoriteRestaurant.objects.all()
    serializer_class = FavoriteRestaurantSerializerGet

# class UserRegister(APIView):
#     def post(self, request):
#         form = RegisterForm()
#         if request.method == 'POST':
#             form = RegisterForm(request.POST)
#             if form.is_valid(): # if form is valid with all the methods inside the form.py
#                 form.save()
#                 return Response(status=status.HTTP_201_CREATED)

class UserRegister(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		clean_data = validate_data(request.data)
		serializer = UserRegisterSerializer(data=clean_data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.create(clean_data)
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		data = request.data
		assert validate_username(data)
		assert validate_password(data)
		serializer = UserLoginSerializer(data=data)
		if serializer.is_valid(raise_exception=True):
			user = serializer.check_user(data)
			login(request, user)
			return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserLogout(APIView):
    def get(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
    
class UserView(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	## return current user data (username, email)
	def get(self, request):
		serializer = UserSerializer(request.user) ## request.user is the current user
		return Response(serializer.data, status=status.HTTP_200_OK)