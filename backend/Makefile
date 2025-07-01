lint:
	ruff format --check --diff
	ruff check
	flake8 ./src --select=WPS
format:
	ruff format
	ruff check --fix
type-check:
	mypy ./src
