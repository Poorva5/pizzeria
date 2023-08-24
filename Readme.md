# PIZZERIA APP


## Prerequisites

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)
- Python 3.9: [Installation Guide](https://www.python.org/downloads/)
- Django: [Installation Guide](https://docs.djangoproject.com/en/stable/topics/install/)
- Celery: [Installation Guide](https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html)
- Redis: [Installation Guide](https://redis.io/download)
- MySQL: [Installation Guide](https://dev.mysql.com/doc/mysql-installation-excerpt/8.0/en/)


1. Clone this repository:

    git clone git@github.com:Poorva5/pizzeria.git

    cd pizzeria

    pip install virtualenv

    virtualenv venv

    source venv/bin/activate

    cd pizzeria

2. Build and start the Docker containers:

    docker-compose up --build

    docker-compose up -d

    docker-compose exec pizzeria python manage.py makemigrations

    docker-compose exec pizzeria python manage.py migrate

    docker-compose exec pizzeria python manage.py createsuperuser

    docker-compose exec pizzeria python3 manage.py initialize_db 

### Celery Configuration

    Celery tasks are configured in the `celery_app.py` file.

### Database Configuration

    The database settings are located in the `settings.py` file.


### API Documentation

    The documentaion of the api can be accessed on this link
    [API postman collection](https://documenter.getpostman.com/view/19475365/2s9Y5WxNtA)












