from choices import Choices
from json import load


def test_choices():
    with open('choices.json') as f:
        _RULES = load(f)

    choices = Choices(_RULES)

    assert choices.decide_game_names('spock', 'spock') == 0
    assert choices.decide_game_names('spock', 'scissors') == -1
    assert choices.decide_game_names('scissors', 'spock') == 1
