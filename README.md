# recipe-app-api

Recipe API project

for running lint:
docker-compose run --rm app sh -c "flake8"

generate django:
docker-compose run --rm app sh -c "django-admin startproject app ."

generate django app:
docker-compose run --rm app sh -c "python manage.py startapp core"

execute the command method:
docker-compose run --rm app sh -c "python manage.py wait_for_db"

create superuser while docker-compose is up
docker-compose run --rm app sh -c "python manage.py createsuperuser"

To enable precommit:

1. download pre-commit
2. pre-commit install (to install script from .pre-commit-config.yaml)

To authorize in localhost:8000/api/docs

1. create user through /api/user/create/
2. get user token from /api/user/token/
3. click Authorize and type: Token {token return from /api/user/token}
