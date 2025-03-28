
start:
	poetry run python manage.py runserver

migrate:
	docker compose run --rm web poetry run python manage.py migrate

migration:
	docker compose run --rm web poetry run python manage.py makemigrations 

createsuperuser:
	docker compose run  --rm web poetry run python manage.py createsuperuser

compose.start:
	docker compose up --build --force-recreate

compose.migrate:
	docker compose run --rm web poetry run python manage.py migrate