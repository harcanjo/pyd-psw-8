from django.urls import path
from . import views

urlpatterns = [
    path('acessar/', views.acessar)
]
