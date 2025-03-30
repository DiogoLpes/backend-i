start:
	poetry run python manage.py runserver

migrate:
	docker compose run --rm web poetry run python manage.py migrate

migration:
	docker compose run --rm web poetry run python manage.py makemigrations 

createsuperuser:
	docker compose exec web poetry run python manage.py createsuperuser

compose.start:
	docker compose up --build --force-recreate

compose.collectstatic:
	docker compose exec web poetry run python manage.py collectstatic --noinput