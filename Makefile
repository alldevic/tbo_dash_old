#!/usr/bin/make

include .env

SHELL = /bin/sh
CURRENT_UID := $(shell id -u):$(shell id -g)

export CURRENT_UID

up:
	docker-compose up -d
upb:
	docker-compose up -d --force-recreate --build --remove-orphans
down:
	docker-compose down
sh:
	docker exec -it /tbo_backend /bin/sh
migrations:
	docker exec -it /tbo_backend python3 manage.py makemigrations
su:
	docker exec -it /tbo_backend python3 manage.py createsuperuser
logs:
	docker logs /tbo_backend -f
