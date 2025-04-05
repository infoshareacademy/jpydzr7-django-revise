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

### Troubleshooting

* Error: `django.db.utils.OperationalError: (1049, "Unknown database 'django_rest_tutorial_infoshare'")` while running
  `python manage.py migrate`
    * To fix that make sure to create `django_rest_tutorial_infoshare` database before running that command.
    * Django creates database automatically only when running sqlite as
      a [documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial02/) make it
      clear ![mysql_note.png](readme_src/mysql_note.png)
    * You can run file that is in repository `queries\step-2.sql` on your database to make sure it is created.

* if You do not see anything after running django server at http://127.0.0.1:8000/ try to open http://localhost:8000/

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

## Setup Django Rest Framework in Project

* Find `settings.py` file and modify `INSTALLED_APPS` entry