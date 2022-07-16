.PHONY: build-release
build-release:
	docker build -t golang-app-release --target release .

.PHONY: build-ci
build-ci:
	docker build -t golang-app-ci --target ci .

.PHONY: build-dev
build-dev:
	docker build -t golang-app-dev --target dev .


.PHONY: run-dev
run-dev: build-dev
	docker run -it -v $(shell pwd)/:/workspace golang-app-dev bash

.PHONY: install
install: ## go install tools
	cd tools && make install

.PHONY: lint
lint: ## golangci-lint
	$(call print-target)
	golangci-lint run --timeout 5m