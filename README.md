## Using Virtual Environments

View [virtualenvwrapper][1] for more commands and documentation

```python
pip install virtualenvwrapper-win
```

Create a new virtual enverionmen.
```python
mkvirtualenv env [-a project_path] [-r requirements_file] ENV_NAME
```

## Django
### Create a new Django project [myproject] in command line
```
django-admin startproject myproject
``` 

### Create a new application [myapp]
```
python manage.py startapp myapp
```

### Run web server

```
python manage.py runserver
```

> Ignore the warnings about  "18 unapplied migration(s)" at this point. 

Once the server is running, you can view the site by navigating to the following URL on the local web browser: http://127.0.0.1:8000/

### Manipulation of Database
Create you Model first
```python
class Feature(models.Model):
    name: models.CharField(max_length=100)
```

Add your app as new attribute to `INSTALLED_APPS` in `settings.py`
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp' #add here
]
```

To make migrations, run command `python manage.py makemigrations`
```
(venv) C:\Users\myproject>python manage.py makemigrations
Migrations for 'myapp':
  myapp\migrations\0001_initial.py
    - Create model Feature
```

To apply migrations, then run `python manage.py migrate`
```
(venv) C:\Users\myproject>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, myapp, sessions
Running migrations:
  ...
  Applying myapp.0001_initial... OK
  ...
```

Register your models in `myapp/admin.py`, then the new model can be manipulated in admin panel
```python
from .models import Feature # Import the model you just created
# Register you models here
admin.site.register(Feature) 
```

### Admin page
- URL:  http://127.0.0.1:8000/admin
- create an user using `python manage.py createsuperuser`

### User Registration In Django
- URL: http://127.0.0.1:8000/register
- `POST` method
- Check if specific input already exists in DB: 
    ```python
    if User.objects.filter(email=email).exists():
    ````
- Create User using Django authentication system and `User` model:
    ```python
    user = User.objects.create_user(username=username, password=password) 
    user.save()
    ```

### User Login And Logout in Django
- URL: http://127.0.0.1:8000/login
```python
from django.contrib.auth.models import auth
# Authentication
user = auth.authenticate(username=username, password=password)
# Login request
auth.login(request, user)
# Logout request
auth.logout(request)
# Check authentication
user.is_authenticated
```

### Dynamic URL Routing
```python
# myapp/urls.py
urlpatterns = [
     path('post/<str:pk>', views.post, name='post')
]

# myapp/views.py
def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
```

## Postgresql Setup
1. install library
```
pip install psycopg2
pip install Pillow
```
2. Set your Database credentials in `myproject/settings.py`
3. Apply migrations
```
python manage.py makemigrations
python manage.py migrate
```

<!-- URL below -->
[1]:https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#managing-environments