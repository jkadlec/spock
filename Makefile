build:
	docker-compose build

down:
	docker-compose down -v

up:
	docker-compose up

check:
	flake8 --max-line-length=120 .
	mypy .
