# Проект Foodgram
Cайт Foodgram, «Продуктовый помощник».
На этом сервисе пользователи смогут публиковать рецепты, подписываться 
на публикации других пользователей, добавлять понравившиеся рецепты в 
список «Избранное», а перед походом в магазин скачивать сводный список 
продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

# Установка
Склонируйте репозиторий.
В корневой директории создайте файл `.env` со следующим содержанием:
```
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=  # ваш вариант
POSTGRES_PASSWORD=  # ваш вариант
DB_HOST=db
DB_PORT=5432
SECRET_KEY= # секретный ключ django проекта
```

Для запуска сервера на локальной машине выполните команды:
```
Первый запуск
docker-compose up -d
после запуска контейнеров
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input

Последующие запуски
docker-compose up -d

```
Документацию к проекту можно посмотреть на странице `api/docs`.
Администрирование доступно на странице `/admin`.
Проект будет запущен и доступен по адресу [localhost](http://localhost).

Ознакомиться с уже развёрнутым проектом можно по адресу [Foodgram](http://localhost).

![Foodgram workflow](https://github.com/grand-roman/foodgram-project-react/actions/workflows/main.yml/badge.svg)
