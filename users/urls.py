from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Страница регистрации
    path('profile/', views.profile, name='profile'),  # Страница входа
]

