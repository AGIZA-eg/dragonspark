# gpaapp/urls.py
from django.urls import path
from .views import calculate_gpa

urlpatterns = [
    path('calculate_gpa/', calculate_gpa, name='calculate_gpa'),
]
