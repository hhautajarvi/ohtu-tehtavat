import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.response = requests.get(url).json()

    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(
                player_dict['name'], player_dict['team'], player_dict['goals'], player_dict['assists'], player_dict['nationality']
            )
            players.append(player)
        return players