from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='account-home'),
    path('about/', views.about, name='account-about'),
    path('register', views.register, name='account-register'),
]
