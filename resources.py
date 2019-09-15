from functools import lru_cache
from flask import current_app as app, request
from flask_restful import Resource

from random_choice import get_random_choice


class ChoicesResource(Resource):

    @lru_cache(maxsize=1)
    def get(self):
        sorted_choices = app.choices.get_sorted_ids()

        ret = []
        for choice_id, choice_name in sorted_choices:
            ret.append({'id': choice_id, 'name': choice_name})

        return ret, 200


class ChoiceResource(Resource):

    def get(self):
        try:
            choice_id = get_random_choice(app.choices.get_max_choice())
        except Exception as e:
            app.logger.error('Random number API failed with', e)
            return {'error': 'cannot get random number'}, 500

        choice_name = app.choices.get_choice_name_by_id(choice_id)

        return {'id': choice_id, 'name': choice_name}


class RoundResource(Resource):

    def post(self):
        if not request.json or 'player' not in request.json:
            return {'error': 'player choice not present'}, 400
        player_choice_id = request.json['player']
        try:
            computer_choice_id = get_random_choice(app.choices.get_max_choice())
        except Exception as e:
            app.logger.error('Random number API failed with', e)
            return {'error': 'cannot get random number'}, 500

        result = app.choices.decide_game(player_choice_id, computer_choice_id)
        if result == -1:
            result = 'win'
        elif result == 0:
            result = 'tie'
        else:
            result = 'lose'

        return {'results': result, 'player': player_choice_id, 'computer': computer_choice_id}
