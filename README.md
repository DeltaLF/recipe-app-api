# recipe-app-api

Recipe API project

for running lint:
docker-compose run --rm app sh -c "flake8"

generate django:
docker-compose run --rm app sh -c "django-admin startproject app ."

To enable precommit:

1. download pre-commit
2. pre-commit install (to install script from .pre-commit-config.yaml)
