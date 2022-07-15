.PHONY: install
install: ## go install tools
	$(call print-target)
	cd tools && go install $(shell cd tools && go list -f '{{ join .Imports " " }}' -tags=tools)

.PHONY: lint
lint: ## golangci-lint
	$(call print-target)
	golangci-lint run --timeout 5m

.PHONY: build-release
build-release:
	docker build -t golang-app --target release .

.PHONY: build-ci
build-ci:
	docker build -t golang-app --target ci .

.PHONY: build-dev
build-dev:
	docker build -t golang-app --target dev .