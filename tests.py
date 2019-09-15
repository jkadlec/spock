from choices import Choices
from json import load


def test_choices():
    with open('choices.json') as f:
        _RULES = load(f)

    choices = Choices(_RULES)

    assert choices.get_sorted_ids() == [(1, 'rock'), (2, 'paper'), (3, 'scissors'), (4, 'spock'), (5, 'lizard')]

    assert choices.decide_game_names('spock', 'spock') == 0
    assert choices.decide_game_names('spock', 'scissors') == -1
    assert choices.decide_game_names('scissors', 'spock') == 1
