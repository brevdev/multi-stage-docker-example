.PHONY: build-release
build-release:
	docker build -t python-app-release --target release .

.PHONY: build-ci
build-ci:
	docker build -t python-app-ci --target ci .

.PHONY: build-dev
build-dev:
	docker build -t python-app-dev --target dev .


.PHONY: run-dev-outer
run-dev-outer: build-dev
	docker run -it -v $(shell pwd)/:/workspace python-app-dev

.PHONY: run-dev-inner
run-dev-inner: build-dev
	docker run -it -v $(shell pwd)/:/workspace python-app-dev bash

.PHONY: run-reload
run-reload:
	poetry run uvicorn python_app.main:app --reload

.PHONY: lint
lint:
	poetry run mypy .

.PHONY: format
format:
	poetry run black .

.PHONY: test
test:
	poetry run pytest .
