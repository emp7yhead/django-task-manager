install:
	@poetry install

migrate:
	@poetry run python manage.py migrate

start:
	@poetry run python manage.py runserver

secret:
	@python -c 'import secrets; print(secrets.token_hex())'

requirements.txt: poetry.lock
	@poetry export -f requirements.txt --output requirements.txt --without-hashes