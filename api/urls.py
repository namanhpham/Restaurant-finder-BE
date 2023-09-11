from django.urls import path
from . import views
from .views import FavoriteRestaurantView

urlpatterns = [
    path('', views.index, name='index'),
    path('favorites/', FavoriteRestaurantView.as_view(), name='favorites')
]