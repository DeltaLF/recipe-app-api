# recipe-app-api

Recipe API project

for running lint:
docker-compose run --rm app sh -c "flake8"

generate django:
docker-compose run --rm app sh -c "django-admin startproject app ."
