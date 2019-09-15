from random import seed, randint
from config import Config as conf
from requests import get

seed()


def get_random_choice(max_val, random_type=conf.RANDOM_GENERATOR_TYPE):
    '''Returns random number from 1 to max_val.'''

    if random_type == 'local':
        return randint(1, max_val)
    elif random_type == 'http':
        # Only this value supported, with arbitrary values the approach below wouldn't work.
        assert conf.RANDOM_GENERATOR_MAX_VAL == 100

        ret = get(conf.RANDOM_GENERATOR_URI)
        ret.raise_for_status()

        if 'random_number' not in ret.json():
            raise KeyError('Random API did not return random_number field.')

        to_normalize = ret.json()['random_number']

        ranges = {range(1, 21): 1, range(21, 41): 2, range(41, 61): 3, range(61, 81): 4, range(81, 101): 5}
        for r, ret_val in ranges.items():
            if to_normalize in r:
                return ret_val
        else:
            raise KeyError('Random API number not in range.')
    else:
        raise KeyError(f'Random type {random_type} not supported.')
