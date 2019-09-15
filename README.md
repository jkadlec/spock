TLDR: `make build`, `make upd`, `pip3 install requests`, `python3 client.py http://localhost:8081`, `make down`

BUILD:
 - `make build`, requires Docker and docker-compose (pip3 install docker-compose)

CONFIGURATION:
 - see server_settings.env. Set RANDOM_GENERATOR_TYPE to local to use randint instead of the API
 - change rules in "choices.json"
 - see docker-compose.yml to change port

TESTS:
 - `make test`: just unittest for the choices class (tests the rules from here: http://www.samkass.com/theories/RPSSL.html , if you change the rules the tests will fail)
 - `make check`: PEP8 and mypy

CLIENT:
 - simple client is in `client.py`, there's just one command line parameter, the url to the server.
 - The client is not dockerized, you'll need the requests library to run it.

TODO: better docs (hopefully most of the code is self-documenting), tests for other classes/files, rate limiting, nginx, scoreboard
