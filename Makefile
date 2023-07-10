.PHONY: bash shell build up down destroy

bash:
	docker compose exec web bash

shell:
	docker compose exec web python

build:
	docker-compose --env-file .env up -d
up:
	docker-compose up

down:
	docker-compose down

destroy:
	docker-compose down -v
