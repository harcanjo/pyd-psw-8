from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def acessar(request):
    return render(request, 'acessar.html')


def criar_curso(request):
    if request.method == "GET":
        return render(request, 'criar_curso.html')
    elif request.method == "POST":
        nome_curso = request.POST.get('nome_curso')
        carga_hora = request.POST.get('carga_hora')
        return HttpResponse(f'{nome_curso} - {carga_hora}')
