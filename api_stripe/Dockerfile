FROM python:3.7-slim

WORKDIR /code

COPY . .

RUN pip3 install -r ./requirements.txt --no-cache-dir

CMD gunicorn api_stripe.wsgi:application --bind 0.0.0.0:8000