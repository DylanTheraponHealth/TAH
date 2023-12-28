from django.urls import path

from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('diabetes/', views.diabetes, name='diabetes'),
    path('charts/', views.pie_chart, name='member'),
]