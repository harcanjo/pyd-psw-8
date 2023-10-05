from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

# Create your views here.


def acessar(request):
    return render(request, 'acessar.html')


def criar_curso(request):
    if request.method == "GET":
        return render(request, 'criar_curso.html')
    elif request.method == "POST":
        nome_curso_form = request.POST.get('nome_curso')
        carga_hora_form = request.POST.get('carga_hora')

        curso = Curso(
            nome_curso=nome_curso_form,
            carga_hora=carga_hora_form,
            data_criacao=datetime.now()
        )

        curso.save()

        return HttpResponse(f'Salvo')
