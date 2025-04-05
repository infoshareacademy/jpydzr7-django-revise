# Django Revise

## Step 1 Changes:

* [Create django project](#Create-Django-Project)

## Step 2 Changes:

* [Setup MySQL Connection in Application](#Setup-MySQL-Connection)
* [Add Django Rest Framework in Project](#Setup-Django-Rest-Framework-in-Project)
* Run command `python manage.py migrate` to migrate django default tables it should look like that <br />
---
![db_structure.png](readme_src/db_structure.png)

---

* Run command `python manage.py runserver` to check if app is running
* After running django server You can open http://127.0.0.1:8000/ and that should be the result

---
![django_welcome_page.png](readme_src/django_welcome_page.png)

---

## Step 3 Changes:

* Create **Password Manager** App in project, running command `python manage.py startapp password_manager` Project structure should look like this <br />
---
![step-2-project-structure.png](readme_src/step-2-project-structure.png)

---
* [Add created app to project settings.py in `INSTALLED_APPS`](#Adding-New-App-To-Project)
* [create `urls.py` file inside `password_manager` app](#Adding-Urls-from-App-to-Project)
* [create `PasswordData` model inside models.py](#Create-Model-inside-App)
* [create basic view inside `views.py`](#Create-django-view)
* [create `templates/index.html` inside `password_manager` and use it as view](#Working-with-templates)

## Step 4 Changes:
* Create View for listing password entries
* Create Form for adding password entries

### Troubleshooting

* Error: `django.db.utils.OperationalError: (1049, "Unknown database 'django_rest_tutorial_infoshare'")` while running
  `python manage.py migrate`
    * To fix that make sure to create `django_rest_tutorial_infoshare` database before running that command.
    * Django creates database automatically only when running sqlite as
      a [documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial02/) make it
      clear ![mysql_note.png](readme_src/mysql_note.png)
    * You can run file that is in repository `queries\step-2.sql` on your database to make sure it is created.

* if You do not see anything after running django server at http://127.0.0.1:8000/ try to open http://localhost:8000/
* When You create new app and pass `urls.py` from app to main `django_rest_tutorial_infoshare/urls.py`, you might lose your welcome page, the reason is that it is not declared in your app directly. It is normal behavior. Your index (starting) page, would probably look something like this <br /> ![welcome_page_not_found.png](readme_src/welcome_page_not_found.png)

## How to run a project step by step

1. Install Django using pip `pip install Django` (or `pip3 install Django`)
2. [Install MySQL](#MySQL-Installation-Guide)
3. install Django_Rest_framework using pip `pip install djangorestframework` (or `pip3 install djangorestframework`)
4. Install python mysqlclient using pip `pip install mysqlclient` (or `pip3 install mysqlclient`)
5. [Create django project](#Create-Django-Project)
6. [Modify database dictionary to set up MySQL Connection](#Setup-MySQL-Connection)
7. [Add Django Rest Framework in Project](#Setup-Django-Rest-Framework-in-Project)
8. Run django project using command `python manage.py runserver` (or `python3 manage.py runserver`)

## MySQL Installation Guide

1. Install MySQL From website https://dev.mysql.com/downloads/installer/
2. If You are using windows

## Create Django Project

* Using django admin `django-admin startproject mysite django_rest_tutorial_infoshare`
* Using Pycharm

## Setup MySQL Connection

* Find `settings.py` file and modify `DATABASES` entry

```python
PROJECT_NAME = 'django_rest_tutorial_infoshare'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': PROJECT_NAME,
        'USER': 'django_user',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
* In `'default'` key change `ENGINE` to `django.db.backends.mysql`, make sure that you have `mysqlclient` installed using `pip install mysqlclient`.
* Setup `NAME`, `USER`, `PASSWORD`, `HOST` and `PORT` as it is in example. Make sure that you know your user name to database and password, for me, it is `django_user` and `root`.

## Setup Django Rest Framework in Project

* Find `settings.py` file and modify `INSTALLED_APPS` entry and put there `'rest_framework'` like in example
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]
```

## Adding New App To Project

* Open `settings.py` file in project
* Find `INSTALLED_APPS` dictionary
* Add link to config file to newly added to project app <br /> ![add_app_config_to_installed_apps.png](readme_src/add_app_config_to_installed_apps.png)

## Adding Urls from App to Project
* Create `urls.py` file inside `password_manager` app <br /> ![urls_in_password_manager_app.png](readme_src/urls_in_password_manager_app.png)
* in `password_manager/urls.py` set `urlpatterns` list (it can be empty for now, example presents finished path with views, it is going to be made later in **Step 3**)<br /> ![initial_urlpatterns_password_manager.png](readme_src/initial_urlpatterns_password_manager.png)
* import `password_manager/urls.py` into project `urls.py` <br /> ![root_urls_initial_password_manager.png](readme_src/root_urls_initial_password_manager.png)

## Create Model inside App
* Open `password_manager/models.py`
* There create new model class, for example PasswordData:
```python
from django.contrib.auth.models import User
from django.db import models

class PasswordData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"service: {self.service_name} (username: {self.username}, email: {self.email}. password: {self.password})"
```
* run command `python manage.py makemigrations` to create database reflection of the created models.
* to set tables into database run `python manage.py migrate` or if You would like to see all queries run `python manage.py sqlmigrate`.
* After that `django_rest_tutorial_infoshare` database should look like this, it should have new table called `password_manager_passworddata` <br /> ![password_manager_passworddata_database_ref.png](readme_src/password_manager_passworddata_database_ref.png)
* `password_manager_passworddata` should have every field that was declared inside `models.py` <br /> ![data_in_password_manager_passworddata.png](readme_src/data_in_password_manager_passworddata.png)

## PasswordData - explanation
 
PasswordData model class represents every entry in password manager.

```python
from django.contrib.auth.models import User
from django.db import models

class PasswordData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"service: {self.service_name} (username: {self.username}, email: {self.email}. password: {self.password})"
```

fields explanation:
* `user` - reflects foreign key from base django `User` class. It is used to make connection between user and password data, in case if more users would use that app.
* `service_name` - represents service name, it is simple string value and from database perspective it has limit for 100 characters.
* `username` - represents username, some apps uses auth option different from email, that field reflects this kind of situation
* `email` - user email, used to login into given service
* `password` - password used to login into given service
* `created_at` - represents date of entry creation
* `__str__` - function that returns couple of field values

## Create django view
* In `password_manager/views.py` set function that represents view that will be visible for user, it can be something like that:
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Password Manager")
```
* every view function needs one parameter, it is conventionally named `request`, and it has to return `HttpResponse` object.
* `HttpResponse` can be filled with multiple values like, data from models, templates, etc. For this example we simply return string.
* When we create that kind of view we set it in `password_manager/urls.py`. Where `views.index` is a name of function that we just created but passed into `path`. <br /> ![views_path_index.png](readme_src/views_path_index.png)
* It tells django to render that view when user opens http://127.0.0.1:8000/password-manager/.
* When we open that page we should see something like that <br /> ![password-manager-app-index-file.png](readme_src/password-manager-app-index-file.png)


## Working with templates
* Templates can be used to render view with some values.
* If You would like to use templates you need to create `templates` directory inside `password_manager` app. 
* `TEMPLATES` variable inside `settings.py` tells django that it should look for `templates` folder in every app, You don't need to change anything there.
* In `templates` we can create all html files. For example `index.html` <br /> ![index_html_structure.png](readme_src/index_html_structure.png)
* Inside `index.html` file we setup base html structure like that
```html
<html lang="pl">
<head>
    <title>Password Manager Welcome Page</title>
</head>
<body>
    <div>
        This is index page for Password Manager...
    </div>
</body>
</html>
```
* Next step would be to create view for that in `password_manager/views.py`  
```python
from django.http import HttpResponse
from django.template import loader

def template_index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))
```
* Right now created function called `template_index`.
* We load our index.html with template loader `from django.template import loader`
* Then return `HttpResponse` object like in previous example, but this time we use `render` function to tell django that we are going to present web page to user.
* `render.template` function require two parameters, first one is `context` that represents values from database that will be presented to user (but can be also an empty object if we are not going to present anything), second parameter is our index.html `template`. 
* last step is to set our `template_index` inside `password_manager/urls.py`
```python
from django.urls import path

from password_manager import views

urlpatterns = [
    path('template-index/', views.template_index, name='template_index'),
]
```
* It is same example like with `views.index`, but this time we use here view that is loaded from template.
* When we visit page http://127.0.0.1:8000/password-manager/template-index/, we should see something like that <br /> ![template_index_view_page.png](readme_src/template_index_view_page.png)