from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

# Create your views here.


def acessar(request):
    return render(request, 'acessar.html')


def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')

        return render(request, 'criar_curso.html', {'status': status})
    elif request.method == "POST":
        nome_curso_form = request.POST.get('nome_curso')
        carga_hora_form = request.POST.get('carga_hora')

        curso = Curso(
            nome_curso=nome_curso_form,
            carga_hora=carga_hora_form,
            data_criacao=datetime.now()
        )

        curso.save()

        return redirect('/cursos/criar_curso/?status=1')


def listar_cursos(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    carga_horaria = request.GET.get('carga_horaria')

    cursos = Curso.objects.all()

    if nome_filtrar:
        cursos = cursos.filter(nome_curso__contains=nome_filtrar)
    if carga_horaria:
        cursos = cursos.filter(carga_hora__gte=carga_horaria)

    return render(request, 'listar_cursos.html', {'cursos': cursos})


def ver_curso(request, id):
    curso = Curso.objects.get(id=id)

    return render(request, 'ver_curso.html', {'curso': curso})
