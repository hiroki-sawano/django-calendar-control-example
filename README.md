# django-calendar-control-example

## Prerequisite

python >= 3.6

## Installation

```
$ python -m venv venv
$ . ./venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Available URL patterns

* `/app/my-model/new` : creates a MyModel object
* `/app/my-model/<int:pk>` : updates a MyModel object
* `/app/my-model/search` : selects a subset of MyModel objects
