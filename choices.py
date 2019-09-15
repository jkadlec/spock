from typing import List, Dict


class Choices(object):

    def __init__(self, rules: Dict[str, Dict]):
        '''Prebuilds all possible winning combinations.'''
        self.choice_id_to_name = {v['id']: name for name, v in rules.items()}
        self.name_to_choice_id = {name: v['id'] for name, v in rules.items()}

        self.min_id, self.max_id = min(self.choice_id_to_name.keys()), max(self.choice_id_to_name.keys())
        if self.min_id != 1:
            raise ValueError('Wrong input dict')

        self.winning_combinations = set()
        for rule_owner, rules in rules.items():
            rules = rules['destroys']
            owner_id = self.name_to_choice_id[rule_owner]
            rule_ids = (self.name_to_choice_id[rule] for rule in rules)
            for rule_id in rule_ids:
                self.winning_combinations.add((owner_id, rule_id))

    def decide_game(self, player_choice_id: int, computer_choice_id: int):
        if player_choice_id == computer_choice_id:
            return 0

        if (player_choice_id, computer_choice_id) in self.winning_combinations:
            return -1
        else:
            return 1

    def decide_game_names(self, player_choice_name: str, computer_choice_name: str):
        player_choice_id = self.name_to_choice_id[player_choice_name]
        computer_choice_id = self.name_to_choice_id[computer_choice_name]

        return self.decide_game(player_choice_id, computer_choice_id)

    def choice_range(self):
        return self.min_id, self.max_id
