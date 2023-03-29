from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
]
