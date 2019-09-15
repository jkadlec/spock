#! /usr/local/bin/python3

from requests import get, post
from sys import argv


def main(uri):
    choices = get(uri + '/api/v0.1/choices')
    choices.raise_for_status()
    choices = choices.json()
    print('You have the following choices:\n',
          '\n'.join(ch['name'] + ': ' + str(ch['id']) for ch in choices))

    names_to_ids = {ch['name']: ch['id'] for ch in choices}
    ids_to_names = {ch['id']: ch['name'] for ch in choices}

    print('make your choice: (type "END" to quit)')

    inp = ''
    while True:
        inp = input()
        if inp == 'END':
            break
        if inp not in names_to_ids:
            print('unknown choice')
        else:
            choice_id = names_to_ids[inp]
            r = post(uri + '/api/v0.1/play', json={'player': choice_id})
            r.raise_for_status()
            r = r.json()

            result = r['results']
            your_choice = ids_to_names[r['player']]
            computer_choice = ids_to_names[r['computer']]

            print(f'result is: {result} (your choice: {your_choice}, computer choice: {computer_choice})')


if __name__ == '__main__':
    main(argv[1])
