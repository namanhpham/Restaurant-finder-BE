from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import FavoriteRestaurantView, UserRegister, UserLogin, UserLogout, UserView

urlpatterns = [
    path('', views.index, name='index'),
    path('favorites/', FavoriteRestaurantView.as_view(), name='favorites'),
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
]