# Django_middleware

django_middleware is backend-practice repository exploring custom and built-in Django middleware. It focuses on the request/response lifecycle, observability, security headers, and error handling.

## Features

1. Custom Django middleware implementation
2. Basic Django native authentication
3. Request / Response processing
4. Custom Error handlind
5. Django templates ( HTML pages )

## Tech Stack

. python 
. Django
. HTML

## Pre-Requisites

. Python 3.10 or newer
. pip
. Virtual environment support

## Project structure

```text
django_middleware/
|-- app/
|   |-- migrations/
|   |   |-- 0001_initial.py
|   |   `-- __init__.py
|   |-- templates/
|   |   `-- app/
|   |       |-- index.html
|   |       `-- login.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- middlewares.py
|   |-- models.py
|   |-- tests.py
|   |-- urls.py
|   `-- views.py
|-- django_middleware/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- .gitignore
|-- db.sqlite3
|-- manage.py
|-- README.md
`-- requirements.txt
```


## Installation

1. Clone the repo
```bash
git clone https://github.com/david-kajinake/django-middleware.git
cd django-middleware

```

2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Apply Database migrations
```bash
python manage.py migrate
```

5. Run Development server
```bash
python manage.py runserver
```

## Middleware Topics

This repository demonstrates middleware concepts such as:

* Processing requests before a view executes
* Modifying responses before they reach the client
* Measuring request duration
* Adding observability metadata
* Implementing security headers
* Handling or logging exceptions
* Returning custom error responses