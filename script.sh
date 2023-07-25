python manage.py makemigrations
python manage.py migrate
celery -A django_profiles worker -l info
python manage.py runserver 0.0.0.0:8080