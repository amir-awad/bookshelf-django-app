FROM python:3.10

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

RUN pip3 install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8080