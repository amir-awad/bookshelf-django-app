# Django-app

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

### Now you can access the Django application by visiting http://localhost:8080 in your web browser.

