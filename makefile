install:
	@poetry install

migrate:
	@poetry run python manage.py migrate

start:
	@poetry run python manage.py runserver

shell:
	@poetry run python manage.py shell

lint:
	@poetry run flake8 task_manager

test:
	@poetry run coverage run --source='.' manage.py test task_manager/tests

test-coverage:
	@poetry run coverage report

test-coverage-report-xml:
	@poetry run coverage xml

check:
	@lint test requirements.txt

secret:
	@python -c 'import secrets; print(secrets.token_hex())'

requirements.txt: poetry.lock
	@poetry export -f requirements.txt --output requirements.txt --without-hashes