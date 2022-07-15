.PHONY: install
install: ## go install tools
	$(call print-target)
	go install $(shell go list -f '{{ join .Imports " " }}' -tags=tools)
