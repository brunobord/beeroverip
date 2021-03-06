# How to install BeerOverIP

At the moment, Beer Over IP is written for Django 1.2, which was the latest stable release at the time the project was started. Migration onto more recent Django versions is planned, but not yet.

## Setup a Django app

You must know how to create the project, right? Easy:

```bash
$ django-admin startproject website
```

`website` is the name of the project I'm going to use all along. Of course, you can use another one by adapting the provided procedure to your needs.

### Checking out beeroverip code

You can fork the repository using the Github interface.

Inside your project, type the command:

```bash
$ git clone git@github.com:<yournick>/beeroverip.git beers
```

This should download the `beers` code from master.

### Change settings

Many parameters need to be changed or added to deliver Beer Over IP. Edit your ``settings.py`` file:

* Select your [database configuration](http://www.djangoproject.com/documentation/0.96/tutorial01/#database-setup), time zone, language, etc.
* Define `MEDIA_URL`. This URL should point at the ``beers/media/`` directory which is inside your project directory (website). You may want to serve it using a lightweight HTTP server. More on [static file serving](http://www.djangoproject.com/documentation/0.96/static_files/) in the Django docs.


### Template dirs

An easy way to define the template dir goes like this:

```python
import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'beers', 'templates')
)
```

You may want to define it by hand. I don't care, it's whatever you want to do.


### Template context processors

You need them.

```python
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'beers.context_processors.analytics_id',
)
```

### Google Analytics

If you want to use the Google Analytics statistic module, you'll have to define an `ANALYTICS_ID`, like this:

```python
ANALYTICS_ID = 'UA-90876-1'
```

Don't worry, it's not a mandatory feature, even if you don't define this settings variable, BeerOverIP will work.

### Installed apps

Add these to your `INSTALLED_APPS` tuple:

```
'django.contrib.admin',
'beers',
```

### URLS


Append this to your ``urls.py`` file:

```python
urlpatterns += patterns('',
    (r'', include('website.beers.urls')),
)
handler404 = 'website.beers.views.custom_404_view'
```

### Database stuff

Everything should be ready now. Then it's a classic:

```bash
$ python manage.py syncdb
$ python manage.py loaddata data notabeer
```

Now it's ready! You can test your website by serving it the way you want (embedded development server, fcgi, mod_python, etc.)
