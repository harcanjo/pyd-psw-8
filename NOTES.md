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
          <label for="nome-curso" class="form-label">Nome do curso:</label>
          <input type="text" class="form-control" id="nome-curso" />
        </div>
        <div class="mb-3">
          <label for="caga-hora" class="form-label">Carga horária</label>
          <input type="text" class="form-control" id="caga-hora" />
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

## To study more

- Django MVT: Base
- Django Rest Framework: API
- MVT x MVC
- MVT - model view template
- MVC - model view controller
