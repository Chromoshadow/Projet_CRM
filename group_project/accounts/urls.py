from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'welcome_home'),
    path('produits/', views.produits),
]