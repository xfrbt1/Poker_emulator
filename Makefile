format:
	isort . && black .


test:
	pytest -v -s
