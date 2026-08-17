import json
from pathlib import Path
from models.Player import Player
from storage.JsonStorage import JsonStorage


class PlayerManager:
    BASE_DIR = Path(__file__).resolve().parent.parent
    players_file = BASE_DIR / "data" / "players.json"

    def __init__(self):
        self.storage = JsonStorage(self.players_file)

    def create_player(self, name):
        players = self.storage.load()
        player_obj = Player(name)

        players.append(player_obj.to_dict())

        self.storage.save(players)

        return player_obj
    

    def update_player(self, player_obj):
        players = self.storage.load()

        for i, player in enumerate(players, start=0):
            if player["name"] == player_obj.name:
                players[i] = player_obj.to_dict()
                break

        self.storage.save(players)
    

    def find_player(self, name):
            players = self.storage.load()
    
            for player in players:
                if player["name"] == name:
                    return Player.from_dict(player)
    
            return None
