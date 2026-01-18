django-admin startapp quickstart
---
# Django REST Framework Tutorial

> [Official Tutorial Link](https://www.django-rest-framework.org/tutorial/quickstart/)

This guide walks you through creating a simple API to allow admin users to view and edit users and groups in the system.

---

## 1. Setup Basic Django Project

### Create and Activate Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Django and Django REST Framework

```bash
pip install djangorestframework
```

### Start Project and App

```bash
django-admin startproject tutorial .  # Note the trailing '.' character
cd tutorial
django-admin startapp quickstart
cd ..
```

### Project Layout Example

```bash
find .
.
./tutorial
./tutorial/asgi.py
./tutorial/__init__.py
./tutorial/quickstart
./tutorial/quickstart/migrations
./tutorial/quickstart/migrations/__init__.py
./tutorial/quickstart/models.py
./tutorial/quickstart/__init__.py
./tutorial/quickstart/apps.py
./tutorial/quickstart/admin.py
./tutorial/quickstart/tests.py
./tutorial/quickstart/views.py
./tutorial/settings.py
./tutorial/urls.py
./tutorial/wsgi.py
./env
./env/...
./manage.py
```

> **Note:** Creating the app within the project directory helps avoid name clashes with external modules.

### Migrate Database

```bash
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser --username admin --email admin@via-internet.de
```

---

## 2. Serializers

Create `tutorial/quickstart/serializers.py` for data representations:

```python
from django.contrib.auth.models import Group, User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
```

> **Tip:** Hyperlinked relations are good RESTful design, but you can use other relationships as needed.

---

## 3. Views

Edit `tutorial/quickstart/views.py`:

```python
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by("name")
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
```

> **Note:** ViewSets group common behavior and keep logic organized and concise.

---

## 4. URLs

Edit `tutorial/urls.py`:

```python
from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
bash: curl -u admin -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
bash: http -a admin http://127.0.0.1:8000/users/
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
```

> **Tip:** ViewSets registered with a router automatically generate the URL conf for your API.

---

## 5. Pagination

To enable pagination, add to `tutorial/settings.py`:

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}
```

---

## 6. Settings

Add `'rest_framework'` to `INSTALLED_APPS` in `tutorial/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

## 7. Testing the API

Start the server:

```bash
python manage.py runserver
```

### Test with curl

```bash
curl -u admin -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
```

Example response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://127.0.0.1:8000/users/1/",
            "username": "admin",
            "email": "admin@example.com",
            "groups": []
        }
    ]
}
```

### Test with httpie

```bash
http -a admin http://127.0.0.1:8000/users/
```

Example response:

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "email": "admin@example.com",
            "groups": [],
            "url": "http://127.0.0.1:8000/users/1/",
            "username": "admin"
        }
    ]
}
```

### Test in Browser

Go to [http://127.0.0.1:8000/users/](http://127.0.0.1:8000/users/) and log in using the control in the top right corner.

---

## 8. Further Reading

For more in-depth understanding, visit the [official Django REST Framework tutorial](https://www.django-rest-framework.org/tutorial/quickstart/) or browse the API guide.

---

*Documentation built with MkDocs.*