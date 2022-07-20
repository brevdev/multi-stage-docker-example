.PHONY: build-release
build-release:
	docker build -t python-app-release --target release .

.PHONY: build-ci
build-ci:
	docker build -t python-app-ci --target ci .

.PHONY: build-dev
build-dev:
	docker build -t python-app-dev --target dev-service .

.PHONY: dev-up
dev-up: build-dev
	docker run -it -v $(shell pwd)/:/workspace python-app-dev sleep infinity

.PHONY: dev-shell
dev-shell: build-dev
	docker run -it -v $(shell pwd)/:/workspace python-app-dev bash

.PHONY: run-server-reload
run-server-reload:
	poetry run uvicorn python_app.server:app --reload

.PHONY: run-worker-reload
run-worker-reload:
	poetry run watchmedo auto-restart --directory=./ --patterns="*.py" --recursive -- make run-worker

run-worker:
	poetry run python -c 'from python_app import worker; worker.run()'

dev-services-up:
	docker-compose -f docker-compose/helpers.yaml -f docker-compose/services.yaml -f docker-compose/dev.yaml up
	docker-compose down

dev-services-build:
	docker-compose -f docker-compose/helpers.yaml -f docker-compose/services.yaml -f docker-compose/dev.yaml build

.PHONY: lint
lint:
	poetry run mypy .

.PHONY: format
format:
	poetry run black .

.PHONY: test
test:
	poetry run pytest .
