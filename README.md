# task-manager
[![Actions Status](https://github.com/emp7yhead/python-project-lvl4/workflows/hexlet-check/badge.svg)](https://github.com/emp7yhead/python-project-lvl4/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/e5b4a102977d30a7c23e/maintainability)](https://codeclimate.com/github/emp7yhead/python-project-lvl4/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e5b4a102977d30a7c23e/test_coverage)](https://codeclimate.com/github/emp7yhead/python-project-lvl4/test_coverage)

Web app for managing tasks between people. Created with Django and PostgreSQL.

https://empty-task-manager.herokuapp.com/
## Dependencies:
- python = "^3.10"
- Django = "^4.0.4"
- gunicorn = "^20.1.0"
- python-dotenv = "^0.20.0"
- psycopg2-binary = "^2.9.3"
- django-bootstrap4 = "^22.1"
- django-filter = "^22.1"
- rollbar = "^0.16.3"

## Installation:

### via poetry:
- clone repo:
```bash
git clone https://github.com/emp7yhead/python-project-lvl4
cd python-project-lvl4
```
- install dependencies:
```bash
make install
```
- set the values of the environment variables in the .env file.
- initialize migrations:
```bash
make migrate
```
- run app:
```bash
make start
```

