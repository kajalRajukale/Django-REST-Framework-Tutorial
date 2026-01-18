# Django-REST-Framework-Tutorial

From [Quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)


### Setup Basic Django Project

```bash
python3 -m venv .venv
source .venv/bin/activate 
```

```bash
# Install Django and Django REST framework into the virtual environment
pip install djangorestframework
```

```bash
# Set up a new project with a single application
django-admin startproject tutorial .  # Note the trailing '.' character
```

```bash
cd tutorial
django-admin startapp quickstart
cd ..
```


```bash
❯ ppython manage.py migrate
```


```
❯ ppython manage.py createsuperuser --username admin --email admin@via-internet.de
```

```
❯ python manage runserver
```

