.PHONY: bootstrap test lint ci run clean

PYTHON ?= python3

bootstrap:
	./scripts/bootstrap.sh

test:
	$(PYTHON) -m pytest

lint:
	$(PYTHON) -m ruff check src tests

ci:
	./scripts/run_ci_locally.sh

run:
	$(PYTHON) -m app

clean:
	rm -rf .venv dist build .pytest_cache .ruff_cache .coverage htmlcov reports
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
