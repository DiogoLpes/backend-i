start:
	COMPOSE_BAKE=TRUE docker compose up -d --force-recreate --build

down:
	docker compose down --volumes

logs:
	docker compose logs -f 

api-logs:
	docker compose logs -f api

tests:
	docker compose run  --rm --entrypoint="" api poetry run pytest -vvv
	