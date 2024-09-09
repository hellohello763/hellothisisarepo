
.PHONY: format install run

format:
	black .

install:
	pip3 install -r requirements.txt

run:
	python3 hello.py

all: format install run