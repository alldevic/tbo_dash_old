#!/usr/bin/make

include .env

SHELL = /bin/sh
CURRENT_UID := $(shell id -u):$(shell id -g)

export CURRENT_UID

up:
	DEBUGPY=False docker-compose up -d
upb:
	DEBUGPY=False docker-compose up -d --force-recreate --build --remove-orphans
upbd:
	DEBUGPY=True docker-compose up -d  --build
down:
	DEBUGPY=True docker-compose down
sh:
	docker exec -it /tbo_backend /bin/sh
migrations:
	docker exec -it /tbo_backend python3 manage.py makemigrations
su:
	docker exec -it /tbo_backend python3 manage.py createsuperuser
logs:
	docker logs /tbo_backend -f
