# api_stripe
Создание платежных форм для товаров
## **Технологии**

Python 3.7, Django 3.2.15, PostgresQL, Docker, Yandex.Cloud.

## **Запуск проекта**

Необхoдимо скачать проект выполнив команду:

```
git clone https://github.com/PeresadaSvetlana/api_stripe.git
```

Перейти в папку cd infra cоздать файл .env с параметрами:

```
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<имя базы данных postgres>
DB_USER=<пользователь бд>
DB_PASSWORD=<пароль>
DB_HOST=<db>
DB_PORT=<5432>
SECRET_KEY=<секретный ключ проекта django>
STRIPE_PRIVATE_KEY=<секретный ключ stripe>
```
Выполнить команду:

```
docker-compose up -d --build
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input

```

```
Проект запуен на Яндекс.Облаке проверить работу можно по ссылке: http://51.250.20.38/item/1/
```
