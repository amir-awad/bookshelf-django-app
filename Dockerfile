FROM python:3.10

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

RUN chmod +x script.sh

CMD ./script.sh