#!/usr/bin/make

include .env

SHELL = /bin/sh
CURRENT_UID := $(shell id -u):$(shell id -g)

export CURRENT_UID

ifeq ($(DEBUG), True)
	FRONTEND_IMAGE := webclient-dev
else
	FRONTEND_IMAGE := webclient-prod
endif

SERVICES = $(FRONTEND_IMAGE) backend migrate collectstatic postgres nginx redis

export FRONTEND_IMAGE
export SERVICES

up:
	DEBUGPY=False docker-compose up -d $(SERVICES)
upb:
	DEBUGPY=False docker-compose up -d --force-recreate --build --remove-orphans $(SERVICES)
upbd:
	DEBUGPY=True docker-compose up -d  --build $(SERVICES)
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
flogs:
	docker logs /tbo_webclient_dev -f
fclean:
	rm -rf ./webclient/node_modules/ ./webclient/src/node_modules/ ./webclient/package-lock.json ./webclient/yarn.lock ./webclient/yarn-error.log ./webclient/__sapper__/
