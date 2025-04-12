# Django Revise

------

## Step 1 Changes:

* [Create django project](#Create-Django-Project)

------

## Step 2 Changes:

* [Setup MySQL Connection in Application](#Setup-MySQL-Connection)
* [Add Django Rest Framework in Project](#Setup-Django-Rest-Framework-in-Project)
* Run command `python manage.py migrate` to migrate django default tables it should look like that <br />
![db_structure.png](readme_src/db_structure.png)


* Run command `python manage.py runserver` to check if app is running
* After running django server You can open http://127.0.0.1:8000/ and that should be the result

![django_welcome_page.png](readme_src/django_welcome_page.png)

------

## Step 3 Changes:

* Create **Password Manager** App in project, running command `python manage.py startapp password_manager` Project structure should look like this <br /> ![step-2-project-structure.png](readme_src/step-2-project-structure.png)

* [Add created app to project settings.py in `INSTALLED_APPS`](#Adding-New-App-To-Project)
* [create `urls.py` file inside `password_manager` app](#Adding-Urls-from-App-to-Project)
* [create `PasswordData` model inside models.py](#Create-Model-inside-App)
* [create basic view inside `views.py`](#Create-django-view)
* [create `templates/index.html` inside `password_manager` and use it as view](#Working-with-templates)

------

## Step 4 Changes:
* [Use predefined methods to create django user](#Create-Django-User)
* [Create login page](#Create-login-page)
* [Create logout page](#Create-logout-page)
* [Create register page](#Create-register-page)

------

## Step 5 Changes

* [Create user passwords list view](#Create-user-passwords-list-view)
* [Create password entry form](#Create-password-entry-form)

------

## Step 6 Changes

* [Extend default Django User class](#Extend-default-Django-User-class)

------

## Step 7 Changes

* [Make migrations from SQL to Django Models](#Make-migrations-from-SQL-to-Django-Models)

------

## Step 8 Changes

* [Using Mixins with Django Models and Views](#Using-Mixins-with-Django-Models-and-Views)

------

## Troubleshooting

* Error: `django.db.utils.OperationalError: (1049, "Unknown database 'django_rest_tutorial_infoshare'")` while running
  `python manage.py migrate`
    * To fix that make sure to create `django_rest_tutorial_infoshare` database before running that command.
    * Django creates database automatically only when running sqlite as
      a [documentation](https://docs.djangoproject.com/en/3.1/intro/tutorial02/) make it
      clear ![mysql_note.png](readme_src/mysql_note.png)
    * You can run file that is in repository `queries\step-2.sql` on your database to make sure it is created.

* if You do not see anything after running django server at http://127.0.0.1:8000/ try to open http://localhost:8000/
* When You create new app and pass `urls.py` from app to main `django_rest_tutorial_infoshare/urls.py`, you might lose your welcome page, the reason is that it is not declared in your app directly. It is normal behavior. Your index (starting) page, would probably look something like this <br /> ![welcome_page_not_found.png](readme_src/welcome_page_not_found.png)
* If You have problem with creating new user after already setting `PasswordData` to existing one, You need to delete all `migrations` files folder from `password_manager/migrations` like in example below <br />
![remove_migrations](readme_src/remove_migrations.png)<br />
This action also requires to delete database that You already created, so do this only if You didn't make modifications by hands in your database, If You do made some changes to database, make sure to do a backup before deleting it.
Then rerun commands `python manage.py makemigrations` and `python manage.py migrate`, after that everything should be working fine. That is related to that kind of error:
```commandline
ValueError: The field admin.LogEntry.user was declared with a lazy reference to 'password_manager.passworddatauser', but app 'password_manager' doesn't provide model 'passworddatauser'.
The field password_manager.PasswordData.user was declared with a lazy reference to 'password_manager.passworddatauser', but app 'password_manager' doesn't provide model 'passworddatauser'.
```

------

## How to run a project step by step

1. Install Django using pip `pip install Django` (or `pip3 install Django`)
2. [Install MySQL](#MySQL-Installation-Guide)
3. install Django_Rest_framework using pip `pip install djangorestframework` (or `pip3 install djangorestframework`)
4. Install python mysqlclient using pip `pip install mysqlclient` (or `pip3 install mysqlclient`)
5. [Create django project](#Create-Django-Project)
6. [Modify database dictionary to set up MySQL Connection](#Setup-MySQL-Connection)
7. [Add Django Rest Framework in Project](#Setup-Django-Rest-Framework-in-Project)
8. Run django project using command `python manage.py runserver` (or `python3 manage.py runserver`)

------

## MySQL Installation Guide

1. Install MySQL From website https://dev.mysql.com/downloads/installer/
2. If You are using windows

------

## Create Django Project

* Using django admin `django-admin startproject mysite django_rest_tutorial_infoshare`
* Using Pycharm

------

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

------

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

------

## Adding New App To Project

* Open `settings.py` file in project
* Find `INSTALLED_APPS` dictionary
* Add link to config file to newly added to project app <br /> ![add_app_config_to_installed_apps.png](readme_src/add_app_config_to_installed_apps.png)

------

## Adding Urls from App to Project
* Create `urls.py` file inside `password_manager` app <br /> ![urls_in_password_manager_app.png](readme_src/urls_in_password_manager_app.png)
* in `password_manager/urls.py` set `urlpatterns` list (it can be empty for now, example presents finished path with views, it is going to be made later in **Step 3**)<br /> ![initial_urlpatterns_password_manager.png](readme_src/initial_urlpatterns_password_manager.png)
* import `password_manager/urls.py` into project `urls.py` <br /> ![root_urls_initial_password_manager.png](readme_src/root_urls_initial_password_manager.png)

------

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

------

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

------

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

------

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

------

## Create Django User
* user in django can be created using command `python manage.py createsuperuser`
* with shell script `python manage.py shell` 
```python
from django.contrib.auth.models import User

user = User.objects.create_user(username='user_1', password='Test1234!')
user.save()
```
* with custom login template/model/view (that is probably most advanced option)
* using already created by Django `UserCreationForm` that is part of `django.contrib.auth.forms`

------

## Create PasswordDataUser
* with shell script `python manage.py shell` 
```python
from password_manager.models import PasswordDataUser

user = PasswordDataUser.objects.create_user(username='user_1', password='Test1234!')
user.save()
```
* with custom login template/model/view (that is probably most advanced option)
* using already created by Django `UserCreationForm` that is part of `django.contrib.auth.forms`

------

## Create login page
* To login user, we need to create `login.html` in `templates` of our `password_manager` app
```html
<h1>Login form</h1>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
```
This form contains couple of HTML tags: 
- `h1` - represents html header it makes text that is inside of tags bigger.
- `form` - that tag create form and as attribute declares http method that will be used to sent data from form, `POST` in this situation
- `{% csrf_token %}` - is a protection from gathering info about user data (like login/password) from malicious software, like malicious sites that uses cookies to get info about user.
- `{{ form.as_p }}` - that is a Django type shortcut to create all labels and inputs for every field required to login user
- `button` - button is responsible to sent data to `UserCreationForm` and validate it.
 
* next is to use predefined `views` from `auth` library inside `password_manager/urls.py`. It is worth notice here that `template_name` parameter is directing to `templates/login.html` that we just created.
```python
from django.urls import path

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login')
]
```

* last step is to set variable called `LOGIN_REDIRECT_URL` in `settings.py`, it can be dynamic and depend on app but for now we are focusing on redirect user to `index` of `password_manager` app, after successful login.

```python
LOGIN_REDIRECT_URL = '/password-manager/'
```

------

## Create logout page
* Logout is similar to login but this time in `password_manager/urls.py` we are just setting predefined `LogoutView`, without creating any logout template

```python
from django.urls import path

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
```

* and like in login redirection, we need to set redirection point on logout in `settings.py`, variable is called `LOGOUT_REDIRECT_URL` and we are focusing on redirect user to login page after logout.

```python
LOGOUT_REDIRECT_URL = '/password-manager/login/'
```

------

## Create register page
* For registration new users we will be using custom view register form, but we will use inside it predefined `UserCreationForm`
* in `views.py`, we created `register_form` where we are putting data from form in `templates/register.html` to create user. Build in `login` function from `django.contrib.auth` is responsible for login user after registration. User will be redirected to `index.html` after creation. 
```python
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.contrib.auth import login

def register_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")
    else:
        form = UserCreationForm()
    register_template = loader.get_template("register.html")
    context = {"form": form}
    return HttpResponse(register_template.render(context, request))
```
* we need already mentioned template `templates/register.html`. It is very similar to `login.html`.
```html
<h1>Register form</h1>

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Register</button>
</form>
```
* last step is to setup `register_form` inside `password_manager/urls.py`

```python
from django.urls import path

from password_manager import views as password_manager_views

urlpatterns = [
    path('register/', password_manager_views.register_form, name='register'),
]
```
------

## Create user passwords list view
* Listing passwords, just take all `PasswordData`, that belongs to logged-in user and returns it with `password_list.html` in view

```python
from django.contrib.auth.decorators import login_required
from password_manager.models import PasswordData
from django.template import loader
from django.http import HttpResponse

@login_required
def passwords_list(request):
    entries = PasswordData.objects.filter(user=request.user)
    passwords_list_template = loader.get_template("passwords_list.html")
    context = {'entries': entries}
    return HttpResponse(passwords_list_template.render(context, request))
```

* like in previous examples we need setup `urls.py`

```python
from django.urls import path

from password_manager import views as password_manager_views

urlpatterns = [
    path('passwords_list/', password_manager_views.passwords_list, name='passwords_list'),
]
```

* And `passwords_list.html` in `templates`
 
```html
<h2>Passwords list</h2>

<table>
    <tr>
        <th>Service name</th>
        <th>Username</th>
        <th>Email</th>
        <th>Password</th>
        <th>Created at</th>
    </tr>
    {% for entry in entries %}
        <tr>
            <td>{{ entry.service_name }}</td>
            <td>{{ entry.username }}</td>
            <td>{{ entry.email }}</td>
            <td>{{ entry.password }}</td>
            <td>{{ entry.created_at|date:"Y-m-d H:i" }}</td>
        </tr>
    {% empty %}
        <tr>
            <td colspan="4">No passwords</td>
        </tr>
    {% endfor %}
</table>

<p><a href="{% url 'add_password_form' %}">Add new login data</a></p>
```

------
## Create password entry form

* To create new password entry, we need to create new `view`, `add_password_form`, it works similar as register form but this time it setting `PasswordData` model with values from form.
* It is also adding `@login_required` decorator, which informs django that only logged in user can access that form.
```python
from django.contrib.auth.decorators import login_required
from password_manager.models import PasswordData
from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

@login_required
def add_password_form(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        entry = PasswordData(user=request.user,
                             service_name=service_name,
                             username=username,
                             email=email,
                             password=password)
        entry.save()

        return redirect('passwords_list')

    add_password_form_template = loader.get_template("add_password_form.html")
    context = {}
    return HttpResponse(add_password_form_template.render(context, request))
```
* As always view need to be registered in `urls.py`

```python
from django.urls import path

from password_manager import views as password_manager_views

urlpatterns = [
    path('add_password_form/', password_manager_views.add_password_form, name='add_password_form'),
]
```

* And we need a template in `templates/add_password_form.html`. Instead of `{{ form.as_p }}` shortcut, we use custom labels and input, notice that it has to have same `name` attributes like fields in `PasswordData` model.
```html
<h2>Add login data</h2>

<form method="post">
    {% csrf_token %}
    <label for="service_name">Service Name:
        <input type="text" name="service_name" required><br><br>
    </label>
    <label for="username">Username:
        <input type="text" name="username" required><br><br>
    </label>
    <label for="email">Email:
        <input type="text" name="email" required><br><br>
    </label>
    <label for="password">Password:
        <input type="password" name="password" required><br><br>
    </label>
    <button type="submit">Save</button>
</form>

<p><a href="{% url 'passwords_list' %}">Return to passwords list</a></p>
```
------
## Extend default Django User class

* Django creators suggests to use default User for Admin proposes only
* For every other use case documentation suggests to extend `AbstractUser` that is part of `django.contrib.auth.models`
  * Django allows to use own User model as a default one, for this it is required to add new variable called `AUTH_USER_MODEL` to `settings.py`
```python
  AUTH_USER_MODEL = 'password_manager.PasswordDataUser'
```
* Before creating custom User model our database looks like that <br />
![initial_db_before_custom_user.png](readme_src/initial_db_before_custom_user.png)
* Next step is to create our User class in `password_manager/models.py`
```python
from django.contrib.auth.models import AbstractUser

class PasswordDataUser(AbstractUser):
    def __str__(self):
        return f"username: {self.username}, email: {self.email}"
```
* we simply extend `AbstractUser` model that is part of django library to create our `PasswordDataUser`, this user has most of properties from `User` class that we used before. We put only `__str__` function but only to not leave body of class empty.

* do not forget to change user foreign key in `PasswordData` after that change from `User` to `PasswordDataUser`
![password_data_user_in_password_data](readme_src/password_data_user_in_password_data.png)
* Just like it was mentioned before, we need to declare new `User` class in `settings.py`, for that simply put `AUTH_USER_MODEL` in settings file, it can be anywhere in file
```python
AUTH_USER_MODEL = "password_manager.PasswordDataUser"
```
* Last step is to use Django cli (commands) to create migrations and migrate new User class. For that we need two commands:
```commandline
python manage.py makemigrations
python manage.py migrate
```
* After successfully running migrations we should see 3 new tables in our database <br />
![new_password_data_user_db](readme_src/new_password_data_user_db.png)
* If You would like to create user (for testing) that is based on `PasswordDataUser`, you can see a tutorial [here](#Create-PasswordDataUser) 
------
## Make migrations from SQL to Django Models

* If You have existing `django_rest_tutorial_infoshare` database, make a backup of it (if You need to), and remove it
* Run file `step-7.sql` in your database program of choice (Dbeaver, Pycharm etc.)
* To migrations in reverse way, so we already have created database in some sql engine for example, MySQL, we have to setup database like in [this step](#Setup-MySQL-Connection) but in database name set already existing database.
* Then run command `python manage.py inspectdb`, by default command take all tables from existing database and try to map it to `models.py`
* We can set a file where models should be created: `python manage.py inspectdb > password_manager/models.py`
* There is also an option to pass couple of tables that we would like to create as a models and skip every other ones: `python manage.py inspectdb table1 table2`

-----
## Using Mixins with Django Models and Views

* Mixins are specific type of class that can be inherited with different class, for example Model class or View class. It shouldn't be inherited alone but as a specific extension for different class.
* We can create default `abstract` model class for setting all models with default `created_at` and `updated_at` rows in tables, for that we create Mixin called `TimestampMixin`
```python
from django.db import models

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```
* it looks like every model class but it has inner class, that is part of django framework called `Meta`, Meta class allows us to create properties and behaviors for models. For example here we setup `abstract = True`, this property defines that `TimestampMixin` will not be created as table during migrations. It can only be inherited in other models.
* So we can update our `PasswordDataUser` and `PasswordData` model classes, It will looks like this:
```python
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class PasswordDataUser(AbstractUser, TimestampMixin):
    def __str__(self):
        return f"username: {self.username}, email: {self.email}"


class PasswordData(TimestampMixin):
    user = models.ForeignKey(PasswordDataUser, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"service: {self.service_name} (username: {self.username}, email: {self.email}. password: {self.password})"
```
* We are using `TimestampMixin` instead of `models.Model` to extend our models, thanks to that after migrations, our database tables will have new properties: <br />
![mixin_database](readme_src/mixin_database.png)
-----
### Sources:

* https://stackoverflow.com/questions/19189813/setting-django-up-to-use-mysql
* https://radixweb.com/blog/create-rest-api-using-django-rest-framework
* https://docs.djangoproject.com/en/5.1/intro/tutorial01/
* https://www.django-rest-framework.org/tutorial/quickstart/
* https://stackoverflow.com/questions/40802165/have-django-to-automatically-create-database-on-migrate
* https://www.tutorialspoint.com/form-as-p-ndash-render-django-forms-as-paragraph
* https://forum.djangoproject.com/t/showing-method-not-allowed-get-users-logout/26044
* https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
* https://medium.com/@karimdhrif4444/mastering-user-management-comprehensive-guide-to-extending-djangos-user-model-51c2ccd793d4
* http://dev.to/idrisrampurawala/creating-django-models-of-an-existing-db-288m
* https://docs.djangoproject.com/en/5.2/howto/legacy-databases/