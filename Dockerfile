# Stage 1: Build dependencies
FROM python:3.8 AS builder

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Stage 2: Build code
FROM python:3.8

RUN mkdir /app

# Copy installed dependencies from the previous stage
COPY --from=builder /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8080