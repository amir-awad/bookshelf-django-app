# Django-app

## Description

This is a simple Django application that uses PostgreSQL as the database backend.

## Running without docker-compose

### first pull the PostgreSQL image from Docker Hub by running the following command:

```bash
docker pull postgres:latest
```

### Now that the PostgreSQL image is available, run the following command to start a new container and create a new PostgreSQL database:

```bash
docker run -d --name db -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydb -p 5432:5432 postgres:latest

```

### Get the IP address of the PostgreSQL container by running the following command:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' db
```

### Update the database settings in the settings.py file:

```python
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'mydb',
    'USER': 'myuser',
    'PASSWORD': 'mypassword',
    'HOST': '<db_container_ip>',
    'PORT': '5432',
    }
}
```

### Build the Django image by running the following command:

```bash
docker build -t django-app .
```

### Now that the Django image is available, run the following command to start a new container and create a new Django project:

```bash
docker run -p 8080:8080 my-django-app
```

## Running with docker-compose

### Update the database settings in the settings.py file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

### Start the docker-compose stack by running the following command:

```bash
docker-compose up -d --build
```

### To test the connection to the database, follow these steps:

#### Enter the web container bash shell by running the following command:

```bash
docker compose exec web bash
```

#### Run the following command to start the Django shell:

```bash
python manage.py shell
```

#### Run the following commands to test the connection to the database:

```bash
import socket

def test_connection(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    return result

host = 'db'
port = 5432

result = test_connection(host, port)
if result == 0:
    print(f"Successfully connected to {host}:{port}")
else:
    print(f"Failed to connect to {host}:{port}")
```

## Finally, you can access the Django application by visiting http://localhost:8080 in your web browser.

### Here is an example of the env files:

.env:

```bash
Django_PORT=8080
POSTGRES_PORT=5432
PGADMIN_PORT_LOCAL=5050
PGADMIN_PORT_CONTAINER=80
```

.env-pgadmin:

```bash
PGADMIN_DEFAULT_EMAIL=user-name@domain-name.com
PGADMIN_DEFAULT_PASSWORD=your-password
```

.env-postgres:

```bash
POSTGRES_PASSWORD=mypassword
POSTGRES_USER=myuser
POSTGRES_DB=mydb
```
