VE ?= ./ve
REQUIREMENTS ?= requirements.txt
SYS_PYTHON ?= /usr/local/bin/python3.12
PIP ?= ve/bin/pip

build:
	rm -rf $(VE)
	$(SYS_PYTHON) -m venv $(VE)
	$(PIP) install --upgrade pip
	$(PIP) install --requirement $(REQUIREMENTS)

test:
	$(VE)/bin/python -m tests.tests

clean:
	rm -rf $(VE)