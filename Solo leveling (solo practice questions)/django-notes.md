# Setup on the terminal
* first choose the directory where you want to create your django app
* Then use
```zsh
mkdir {foldername}
```
    to create a new folder
    
```zsh
cd {foldername}
```
    to enter the folder



### making a virtual environment
use this code to make a virtual environment


 ```zsh
python3 -m venv {environment name}
```

Then use the following code to activate the virtual environment



```zsh
source {environment name}/bin/activate
```

__to deactivate__

```zsh
deactivate
```


Now, let's install django on the virtual environment


```zsh
pip3 install django
```
Then again, to create a new django app, run following code


```zsh
django-admin startproject {Project name}
```

Then, to start the developmental server, run the following
```zsh
python3 manage.py runserver
```

if the main port (8000) is already activated then you can use the following command
```zsh
python3 manage.py runserver {port_number} 

```
portnumber can be 8001, 8002 etc...


NOTE: the code `pip3 list` gives the list of all packages that have been sucessfully installed


# On code editor (vsCode)
To open the code in vscode use following
```zsh
cd {Project name}
code .
```

You still need to activate the virtual environmet in vscode, to do so, just use the following commands

```zsh
source {environment name}/bin/activate 
```

This must be done in every new power shell you open

NOTE: to open list out all the elements in your current directory, use `ls`

```zsh
ls
``` 
this gives all the files in current directory

# Making a new app in our webapp
Say we have to make our web-app feature packed (like facebook has reels section, chats, news feed, groups and so much more) then we have to make apps within our webapp to make our project more managable. 

So, let's add a new app within our webapp by using following code
```zsh
python3 manage.py startapp {app name}
```
let's say we created a new app, meroApp then
```zsh
python3 manage.py startapp meroApp
```
The new app {meroApp} will have completely dfferent files to that of the original/root app


# Urls and Views
These are necessary for Templating in Django

In our default urls.py file we make a list urlpatterns where we add path

__<p align="center">in urls.py file in the main/root app </p>__

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), #This is provided in tempelate
    path("home/", include("meroApp.urls") ),
    
]
```

in this example, the first parameter represents the string that should be added after the domain name 

eg. `www.mywebsite.com/home/`


This will now redirect the code to meroApp folder and go to urls.py

By default meroApp will not have a urls.py file, so we will create our own urls.py


__<p align="center">in urls.py file in the meroApp app </p>__

```python
from django.urls import path
from .views import home

urlpatterns = [
    path('page1', home)
]
```

Now, the domain that we should use to access home is `www.mywebsite.com/home/page1`

The second parameter in path {i.e home in this case} is a function which is defined in file views.py from meroApp. This function is executed whenever we make https request to `www.mywebsite.com/home/page1`

__<p align="center">in views.py file in the meroApp app </p>__

```python
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def home(request):
    html_request = """
    {html content}
    """
    return HttpResponse(html_content)


```

### V.imp note, everytime you make a new app {meroApp in this case}, you must register the appname in settings.py file in the root app 

Head to {root app} > settings.py > find list called INSTALLED_APPS then add your new app name in the list
```python

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'meroApp' #This is the app name we added
]
```
# Templates

We will now render Html files using templates

For that we first have to create a folder named `templates` {it's absolutely necessary to name is templates} then make another folder inside templates folder. It is a convention to use the same name as the app name then make our html files there. 

so overall

meroApp > {create} templates > {create} meroApp > {create} index.html

Then, it is necessary to mention the directory on the settings.py of the root app. 

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], #This is where we add the directory of the tempelates
        'APP_DIRS': True, #This is set to true to enable django tempelates
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

In this case we don't need to mention the directory of tempelate, if the folder is in a different directory than the we have right now then we gotta mention it. 








