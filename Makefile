
.PHONY: format install run

format:
	black .

install:
	pip install -r requirements.txt

run:
	python hello.py

all: format install run