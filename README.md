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