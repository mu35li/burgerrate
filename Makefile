.PHONY: run setup init-db

run:
	./scripts/run.sh

setup:
	./scripts/setup.sh && ./scripts/venv-setup.sh

init-db:
	./scripts/init-db.sh
