# Notes

## Django intro

- Django é um framework web para desenvolvimento em Python.
- Facilita muito o desenvolvimento, tem muitas funcionalidades prontas.

- Virtual env:

```bash
$ python -m venv venv
```

- Activate venv Windows:

```bash
$ .\venv\Scripts\activate
```

- Install Django:

```bash
$ python pip install django
```

- Create a Django project

```bash
$ django-admin startproject NOMEDOPROJETO
```

Se preferir criar nesta mesma pasta adicione um ponto ao final do comando

```bash
$ django-admin startproject pythonando .
```

- Django project structure:

  - main folder (ex: pythonando):
    - Core Django project files (ex: pythonando/pythonando):
      - \_\_init\_\_.py
      - asgi.py
      - settings.py
      - urls.py
      - wsgi.py
    - manage.py

- Core Django project files:
  - settings.py - configurações gerais do projeto:
    - Debug - se esta em desenvolvimento ou produção
    - Allowed Hosts - quais os dominios da aplicação
    - Installed apps - o que esta instalado
    - Middlewares
    - Templates
    - Databases - ORM
    - Language
    - Static files
  - urls.py - rotas da aplicação
  - asgi.py - aside gateway
  - wsgi.py - web server
  - manage.py - CLI do Django

```bash
$ python manage.py runserver
```

- Django segue o lema "dividir para conquistar", divide o projeto em pequenos problemas, no caso apps, um app para area de membros, ou tela de login.

```bash
$ python manage.py startapp NOMEDOAPP
```

- Django App structure:

  - main app (ex: cursos):
    - migrations folder:
      - \_\_init\_\_.py
    - \_\_init\_\_.py
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - views.py

- Django flow:

  - request:
    -> server (http)
    -> urls.py (routes)
    -> views.py (views/middlewares)
    -> models.py (modelos)
    -> templates (html/css/js)
  - response:
    <- server (http)
    <- views.py (views/middlewares)

- Add new apps to urls.py
  - import include
  - create a path to urlpatterns, like 'cursos'.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', include('cursos.urls')),
]
```

- Add urls.py file inside the app to be included (cursos)
  - the urls.py inside the app

```python
from django.urls import path
from . import views

urlpatterns = [
    path('acessar/', views.acessar)
]
```

- Add the function to the url in the views.py:

```python
from django.shortcuts import render
from django.http import HttpResponse

def acessar(request):
    return HttpResponse('Olá mundo!')
```

- Add the new app (cursos) to the settings.py -> INSTALLED_APPS:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cursos',
]
```

- You need to import 'os' library to the settings.py

```python
import os
```

- Add path of templates folder to DIRS in TEMPLATES section in settings.py

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

- Inside de app (cursos) create a 'templates' folder:

  - create the templete file: acessar.html

- Make the view render the template:

```python
from django.shortcuts import render
from django.http import HttpResponse

def acessar(request):
    return render(request, 'acessar.html')
```

- To add more urls:

**Add url name in urls.py**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('acessar/', views.acessar),
    path('criar_curso/', views.criar_curso),
    path('outro_nome/', views.outro_nome),
]
```

**Add url function views.py**

```python
from django.shortcuts import render
from django.http import HttpResponse

def acessar(request):
    return render(request, 'acessar.html')

def criar_curso(request):
    return render(request, 'criar_curso.html')

def outro_nome(request):
    return render(request, 'outro_nome.html')
```

**Add respective templates (\*.html) to templates folder**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Criar Curso</title>
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
      crossorigin="anonymous"
    />
  </head>

  <body>
    <div class="container">
      <h1>Crie seu curso</h1>
      <hr />

      <form action="">
        <div class="mb-3">
          <label for="nome_curso" class="form-label">Nome do curso:</label>
          <input
            type="text"
            class="form-control"
            id="nome_curso"
            name="nome_curso"
          />
        </div>
        <div class="mb-3">
          <label for="carga_hora" class="form-label">Carga horária</label>
          <input
            type="text"
            class="form-control"
            id="carga_hora"
            name="carga_hora"
          />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </div>
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```

- To use the form action:

```html
<form action="/cursos/criar_curso/" method="POST"></form>
```

- This method post will be used to send form data, in views the get method is used, every time the route is accessed:

```python
def criar_curso(request):
    if request.method == "GET":
        return render(request, 'criar_curso.html')
    elif request.method == "POST":
        return HttpResponse("Teste")
```

- Isso cai na validação de formulário

```html
<form action="/cursos/criar_curso/" method="POST"></form>
{% csrf_token %}
```

- Para ver o que é enviado na requisição, basta adicionar um print na função dentro da views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

def acessar(request):
    return render(request, 'acessar.html')

def criar_curso(request):
    if request.method == "GET":
        return render(request, 'criar_curso.html')
    elif request.method == "POST":
        print(request.POST.get('nome_curso'))
        # print(request.META)
        # print(request))
        return HttpResponse("Teste")
```

- To get this data:

```python
def criar_curso(request):
    if request.method == "GET":
        return render(request, 'criar_curso.html')
    elif request.method == "POST":
        nome_curso = request.POST.get('nome_curso')
        carga_hora = request.POST.get('carga_hora')
        return HttpResponse(f'{nome_curso} - {carga_hora}')
```

- If we want to process this data in database, first we need to make the migrations of Django pre created models first:

```bash
$ python manage.py migrate
```

- To use MVT, in model we use the concept of models, in the models.py file inside app (cursos) folder:

```python
from django.db import models

class Curso(models.Model):
    nome_curso = models.CharField(max_length=40)
    carga_hora = models.IntegerField()
    data_criacao = models.DateField()
    ativo = models.BooleanField(default=True)
```

- To make this model become a table on our database, we need to run the migrations for this model

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- To access /admin: _Create Superuser_

```bash
$ python manage.py createsuperuser
```

- Username: admin
- Email: email@email.com
- Password: admin

- To access our created model through admin, in admin.py add our model

```python
from django.contrib import admin
from .models import Curso

admin.site.register(Curso)
```

- To be able to save form data to db through model, we need to import the model to view:

```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
```

- To get the data we need to instantiate the model in the view

```python

  curso = Curso(
    nome_curso=nome_curso_form,
    carga_hora=carga_hora_form,
    data_criacao=...
  )
```

- To get date and time, we need to import datetime library

```python
from datetime import datetime

(...)

 curso = Curso(
    nome_curso=nome_curso_form,
    carga_hora=carga_hora_form,
    data_criacao=datetime.now(),
  )
```

- To save this data on db, we need to save()

```python
curso.save()
```

- To see our criar_curso complete function:

```python
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
```

- After we save the data, we want to redirect the user back to /criar_curso/ view, and we need to import redirect

```python
from django.shortcuts import render, redirect

        (...)

        curso.save()

        return redirect('/cursos/criar_curso/')
```

- When redirecting, we can add parameters to url using '?'

```python
return redirect('/cursos/criar_curso/?status=1')
```

- We can use these parameters in our code, to test if we are receiving this:

```python
(...)

def criar_curso(request):
    if request.method == "GET":
        status = request.GET
        print(status)

        return render(request, 'criar_curso.html')

        (...)
```

- To send this to our criar_curso.html, we can send this in our render like this:

```python
def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')

        return render(request, 'criar_curso.html', {'status': status})
```

- On our criar_curso.html we need to add:

```html
<body>
  <div class="container">
    <h1>Crie seu curso</h1>
    {{status}}
    <hr />
    (...)
  </div>
</body>
```

- We can show some message if the status = 1:

```html
<body>
  <div class="container">
    <h1>Crie seu curso</h1>
    {% if status == '1' %}
    <h1>Dados salvos com sucesso!</h1>
    {% endif %}
    <hr />
    (...)
  </div>
</body>
```

- We can add bootstrap to improve this visual

```html
<body>
  <div class="container">
    <h1>Crie seu curso</h1>
    {% if status == '1' %}
    <div class="alert alert-success" role="alert">
      Dados salvos com sucesso!
    </div>
    {% endif %}
    <hr />
  </div>
</body>
```

- Now we want to add another view: listar_cursos

- In urls:

```python
urlpatterns = [
    path('acessar/', views.acessar),
    path('criar_curso/', views.criar_curso),
    path('listar_cursos/', views.listar_cursos),
]
```

- In views:

```python
def listar_cursos(request):
    return render(request, 'listar_cursos.html')
```

- And we have to create the 'listar_cursos.html' in templates folder.

- Now to get all cursos in db to show in list we need to get in views.py

```python
def listar_cursos(request):
    cursos = Curso.objects.all()
    print(cursos)

    return render(request, 'listar_cursos.html')
```

- But to get the names, we need to edit our models, and add magic method def \_\_str\_\_

```python
class Curso(models.Model):
    nome_curso = models.CharField(max_length=40)
    carga_hora = models.IntegerField()
    data_criacao = models.DateTimeField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_curso
```

- To send this to our template listar_cursos.html:

```python
return render(request, 'listar_cursos.html', {'cursos': cursos})
```

```html
<body>
  <h1>Listar cursos</h1>
  {{cursos}}
</body>
```

- To list it better

```html
<body>
  <h1>Listar cursos</h1>
  {% for i in cursos %}
  <h3>Nome: {{i.nome_curso}}</h3>
  <h4>Carga horária: {{i.carga_hora}}</h4>
  {% endfor %}
</body>
```

- To create a form filter we added a form to template

```html
<body>
  <div class="container">
    <br />

    <form action="{% url 'listar_cursos' %}" method="GET">
      <div class="mb-3">
        <label for="nome" class="form-label">Nome</label>
        <input type="text" class="form-control" id="nome" name="nome_filtrar" />
      </div>
      <button type="submit" class="btn btn-success" value="filtrar">
        Filtrar
      </button>
    </form>

    <br />
  </div>
</body>
```

- To make this form work we need to, add method to form or add name to urls in urls.py:

```python
urlpatterns = [
    path('acessar/', views.acessar),
    path('criar_curso/', views.criar_curso, name="criar_curso"),
    path('listar_cursos/', views.listar_cursos, name="listar_cursos"),
]
```

- Now, in we add django to action in form

```html
<form action="{% url 'listar_cursos' %}" method="GET">(...)</form>
```

- Now in views.py, a simple filter

```python
def listar_cursos(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    if nome_filtrar:
        cursos = Curso.objects.filter(nome_curso=nome_filtrar)
    else:
        cursos = Curso.objects.all()

    return render(request, 'listar_cursos.html', {'cursos': cursos})
```

- But that will only filter exctly the same value, we need more flexible filter, like

```python
def listar_cursos(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    if nome_filtrar:
        cursos = Curso.objects.filter(nome_curso__contains=nome_filtrar)
    else:
        cursos = Curso.objects.all()

    return render(request, 'listar_cursos.html', {'cursos': cursos})
```

- To filter by time length and name we need to add field to form and change our function in view

```html
<div class="mb-3">
  <label for="carga_hora" class="form-label">Carga Horária</label>
  <input
    type="number"
    class="form-control"
    id="carga_hora"
    name="carga_horaria"
  />
</div>
```

```python
def listar_cursos(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    carga_horaria = request.GET.get('carga_horaria')

    cursos = Curso.objects.all()

    if nome_filtrar:
        cursos = cursos.filter(nome_curso__contains=nome_filtrar)
    if carga_horaria:
        cursos = cursos.filter(carga_hora=carga_horaria)

    return render(request, 'listar_cursos.html', {'cursos': cursos})
```

- To filter by minimum time length we add '\_\_gte' to carga_hora:

```python
if carga_horaria:
        cursos = cursos.filter(carga_hora__gte=carga_horaria)
```

- To filter by maximum time length we add '\_\_tte' to carga_hora:

```python
if carga_horaria:
        cursos = cursos.filter(carga_hora__lte=carga_horaria)
```

- Only greater than \_\_gt
- Only smaller than \_\_lt

- To be able to click in each curso listed in view we need to create another url, this url ver_curso/<int:id> is a dinamic url

```python
urlpatterns = [
    path('acessar/', views.acessar, name="acessar"),
    path('criar_curso/', views.criar_curso, name="criar_curso"),
    path('listar_cursos/', views.listar_cursos, name="listar_cursos"),
    path('ver_curso/<int:id>', views.ver_curso, name="ver_curso"),
]
```

- To make each curso clickable:

```html
{% for i in cursos %}
<h4>Nome: <a href="/curso/ver_curso/{{i.id}}">{{i.nome_curso}}</a></h4>
<h5>Carga horária: {{i.carga_hora}}</h5>
<hr />
{% endfor %}
```

- In views we create this view with the parameter

```python
def ver_curso(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, 'ver_curso.html', {'curso': curso})
```

- In ver_curso.html template

```html
<div class="container">
  <h5>Nome: {{curso.nome_curso}}</h5>
  <h5>Carga Horária: {{curso.carga_hora}}</h5>
  <h5>Data: {{curso.data_criacao}}</h5>
  <h5>Ativo: {{curso.ativo}}</h5>
</div>
```

- To be able to delete this curso, we need a button:

```html
<a href="{% url 'deletar_curso' curso.id %}" class="btn btn-danger">Deletar</a>
```

- To delete we need another url

```python
path('deletar_curso/<int:id>', views.deletar_curso, name="deletar_curso"),
```

- In views

```python
def deletar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect('/cursos/listar_cursos')
```

- If you dont want to delete the course, you can simple make active to false

```python
def deletar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.ativo = False
    curso.save()
    return redirect('/cursos/listar_cursos')
```

- If you dont want to list dont active cursos in listar_cursos.html
```html
```

## To study more

- Django MVT: Base
- Django Rest Framework: API
- MVT x MVC
- MVT - model view template
- MVC - model view controller
