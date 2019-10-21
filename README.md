# Games-api using Django REST Framework
A simple Games-api built using the Django REST Framework (DRF).

## About

A games api using the Django REST Framework (DRF). Shows how to develop RESTful APIs with Django and the Django REST Framework. In particular, the following topics are addressed:

- Virtual environment with Django REST Framework.
- Creating and working with models.
- Django REST Framework serializers.
- Class-based views
- Authentication of APIs in Django
- Testing the API

## Getting Started

### Installation
Clone this repository:

    git clone https://github.com/jonahkuria/games-api.git

Create virtualenv and install all requirements in requirements.txt:

    cd games-api/
    python3 -m venv <venv_name>
    source <venv_name>/bin/activate
    pip install -r requirements.txt

The code in this repository has been developed and tested using `Python 3.7.3`.


Prepare gamesdb database in postgreSQL:

    sudo -u postgres psql
    CREATE DATABASE gamesdb; 

    # Quit postgresql shell
    \q

