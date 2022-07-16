.PHONY: build-release
build-release:
	docker build -t python-app-release --target release .

.PHONY: build-ci
build-ci:
	docker build -t python-app-ci --target ci .

.PHONY: build-dev
build-dev:
	docker build -t python-app-dev --target dev .

.PHONY: run-dev
run-dev: build-dev
	docker run -it -v $(shell pwd)/:/workspace python-app-dev bash

.PHONY: run-reload
run-reload:
	uvicorn python_app.main:app --reload

.PHONY: lint
lint:
	mypy .

.PHONY: format
format:
	black .