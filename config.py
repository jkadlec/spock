from os import getenv


class Config(object):
    APP_NAME = 'RPSSL'
    TEST = False
    RANDOM_GENERATOR_TYPE = getenv('RANDOM_GENERATOR_TYPE', 'local')
    RANDOM_GENERATOR_URI = getenv('RANDOM_GENERATOR_URI')
    RANDOM_GENERATOR_MAX_VAL = int(getenv('RANDOM_GENERATOR_MAX_VAL'))
    RANDOM_GENERATOR_RL = int(getenv('RANDOM_GENERATOR_RL', '100'))  # per second
    RULES_FILE = '/app/worker/choices.json'

    RULES = None
