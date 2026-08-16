import json
from pathlib import Path
from models.Player import Player


class PlayerManager:
    BASE_DIR = Path(__file__).resolve().parent.parent
    players_file = BASE_DIR / "data" / "players.json"

    def __init__(self):
        pass

    def create_player(self, name):
        players = self.load_players()
        player_obj = Player(name)

        players.append(player_obj.to_dict())

        with open(self.players_file, "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4, ensure_ascii=False)

        return player_obj
    

    def load_players(self):
        try:
            with open(self.players_file, "r", encoding="utf-8") as file:
                players = json.load(file)

            if isinstance(players, dict):
                players = [players]

        except (FileNotFoundError, json.JSONDecodeError):
            players = []

        return players


    def update_player(self, player_obj):
        players = self.load_players()

        for i, player in enumerate(players, start=0):
            if player["name"] == player_obj.name:
                players[i] = player_obj.to_dict()
                break

        with open(self.players_file, "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4, ensure_ascii=False)

    def find_player(self, name):
            players = self.load_players()
    
            for player in players:
                if player["name"] == name:
                    return Player.from_dict(player)
    
            return None
