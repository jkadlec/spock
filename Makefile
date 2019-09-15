build:
	docker-compose build

down:
	docker-compose down -v

up:
	docker-compose up

upd:
	docker-compose up -d

check:
	flake8 --max-line-length=120 .
	mypy --ignore-missing-imports .

test:
	docker build -t spock/tests -f Tests_Dockerfile .
	docker run --rm -it spock/tests
