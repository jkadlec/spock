from choices import Choices
from json import load


def test_choices():
    with open('choices.json') as f:
        _RULES = load(f)

    choices = Choices(_RULES)

    assert choices.get_sorted_ids() == [(1, 'rock'), (2, 'paper'), (3, 'scissors'), (4, 'spock'), (5, 'lizard')]

    winning_tuples = (('scissors', 'paper'),
                      ('paper', 'rock'),
                      ('rock', 'lizard'),
                      ('lizard', 'spock'),
                      ('spock', 'scissors'),
                      ('scissors', 'lizard'),
                      ('lizard', 'paper'),
                      ('paper', 'spock'),
                      ('spock', 'rock'),
                      ('rock', 'scissors'))

    assert choices.decide_game_names('spock', 'spock') == 0

    for win, lose in winning_tuples:
        assert choices.decide_game_names(win, lose) == -1
        assert choices.decide_game_names(lose, win) == 1
