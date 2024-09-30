from django.urls import path
from  . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('eventers/', views.eventers, name='eventers'),
    path('eventers/details/<int:id>', views.details, name='details'),
]