from django.urls import path
from . import views

urlpatterns = [
    path('acessar/', views.acessar, name="acessar"),
    path('criar_curso/', views.criar_curso, name="criar_curso"),
    path('listar_cursos/', views.listar_cursos, name="listar_cursos"),
    path('ver_curso/<int:id>', views.ver_curso, name="ver_curso"),
]
