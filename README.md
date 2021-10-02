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

### Maniipulation of Database
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

<!-- URL below -->
[1]:https://virtualenvwrapper.readthedocs.io/en/latest/command_ref.html#managing-environments