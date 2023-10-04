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
  -
