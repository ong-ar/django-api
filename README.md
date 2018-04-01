# django-api

## requirements

python3, pip, pipenv

## settings

```
pip install cookiecutter
```

```
cookiecutter https://github.com/pydanny/cookiecutter-django
```

install in virtual env

```
pipenv --three
pipenv install django
pipenv install requests
```

install python packages

```
pipenv install -r requirements/local.txt
```

use virtual env and run server

```
pipenv shell
python manage.py migrate
python manage.py runserver
```

create app

```
django-admin startapp [app_name]
```

## install jwt

```
pipenv install djangorestframework-jwt
```

add code to base.py

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}
```

add code to urls.py

```python
from rest_framework_jwt.views import obtain_jwt_token
...
url(r'^api-token-auth/', obtain_jwt_token),
```

## install django-rest-auth

```shell
pipenv install django-rest-auth
```

add code to base.py

```python
INSTALLED_APPS = (
    ...,
    'rest_framework',
    'rest_framework.authtoken',
    ...,
    'rest_auth'
)
```

add code to urls.py

```python
url(r'^rest-auth/', include('rest_auth.urls'))
```
