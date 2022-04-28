default: help
docker_run=docker-compose run --rm app

.PHONY: build

help: ## Show this help
	@echo "Targets:"
	@fgrep -h "##" $(MAKEFILE_LIST) | grep ":" | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/\(.*\):.*##[ \t]*/    \1 ## /' | sort | column -t -s '##'
	@echo

env: ## Create .env file based on .env.example
	cp .env.example .env

build: ## Build the images
	docker-compose build --no-cache

up: ## Start the containers
	docker-compose up -d

down: ## Shutdown the containers
	docker-compose down

stop: ## Stop the containers
	docker-compose stop

sh: ## Run new container and connect to shell
	$(docker_run) bash

ssh: ## Connect to running container shell
	docker-compose exec app bash

logs: ## Show logs
	docker-compose logs -f -t app

run: ## Run the application
	@$(docker_run) bash run.sh
