from django.urls import path
from . import views


urlpatterns = [
    path('', views.about_us, name='about_us'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('cookie_policy/', views.cookie_policy, name='cookie_policy'),
    path('terms/', views.terms, name='terms'),
    path('faqs/', views.faqs, name='faqs'),
]
