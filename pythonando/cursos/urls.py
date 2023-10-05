from django.urls import path
from . import views

urlpatterns = [
    path('acessar/', views.acessar),
    path('criar_curso/', views.criar_curso),
    path('listar_cursos/', views.listar_cursos),
]
