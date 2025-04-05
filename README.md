# Django Revise

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