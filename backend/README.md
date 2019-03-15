# HackerTrend Backend 

This is a simple Django project that lists the currently top trending articles from HackerNews.

## Packages used:
```
Django==2.1.5
django-haystack==2.8.1
djangorestframework==3.9.0
elasticsearch==5.5.3
requests==2.21.0
```

## Requirement
```
Python 3.x
Elastic Search v2.4.x
SQLite3
```

## How to install
```
Clone
run `python -m venv venv` to create a virtual environment.
activate virtual environment: `venv\Scripts\activate` (Windows)  `source venv/bin/activate` (Linux).
run `pip install -r requirements.txt` to install required packages.
run `python manage.py migrate` to create DB schema.
run `python manage.py runserver` to start development server.
```
