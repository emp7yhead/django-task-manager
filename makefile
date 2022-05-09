install:
	@poetry install

migrate:
	@poetry run python manage.py migrate

start:
	@poetry run python manage.py runserver

shell:
	@poetry run python manage.py shell

test:
	@poetry run coverage run --source='.' manage.py test task_manager/tests

coverage:
	@poetry run coverage report

secret:
	@python -c 'import secrets; print(secrets.token_hex())'

requirements.txt: poetry.lock
	@poetry export -f requirements.txt --output requirements.txt --without-hashes