from django.urls import path
from . import views


urlpatterns = [
    path('', views.news, name='news'),
    path('add_news/', views.add_news, name='add_news'),
    path('<slug:slug>/', views.news_details, name='news_details'),
    path('edit/<slug:slug>/', views.edit_news, name='edit_news'),
    path('delete/<slug:slug>/', views.delete_news, name='delete_news'),
]