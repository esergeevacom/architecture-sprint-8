THIS_FILE := $(lastword $(MAKEFILE_LIST))
.PHONY: help build up start down destroy stop restart rebuild destroy_all linters format test-rebuild test-restart

help:
	make -pRrq  -f $(THIS_FILE) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

build:
	docker compose -f docker-compose.yaml build $(c)

up:
	docker compose --env-file .env -f docker-compose.yaml up -d $(c)

start:
	docker compose -f docker-compose.yaml start $(c)

down:
	docker compose -f docker-compose.yaml down $(c)

destroy:
	docker compose -f docker-compose.yaml down -v $(c)

stop:
	docker compose -f docker-compose.yaml stop $(c)

restart:
	docker compose -f docker-compose.yaml down $(c)
	docker compose --env-file .env -f docker-compose.yaml up -d $(c)

rebuild:
	docker compose -f docker-compose.yaml down $(c)
	docker compose -f docker-compose.yaml build $(c)
	docker compose --env-file .env -f docker-compose.yaml up -d $(c)

destroy_all:
	docker compose rm -f
	docker rm -vf $$(docker ps -aq)
	docker rmi -f $$(docker images -aq)

format:
	black --verbose --config pyproject.toml api/src
	isort --sp pyproject.toml api/src
	bandit -c pyproject.toml -r api/src
