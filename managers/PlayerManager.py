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

        new_player = {
            "name": name,
            "level":1,
            "xp": 0,
            "total_xp": 0,
            "missions_completed": 0,
            "list_missions_completed": []
        }

        players.append(new_player)

        with open(self.players_file, "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4, ensure_ascii=False)

        player_obj.level = new_player["level"]
        player_obj.xp = new_player["xp"]
        player_obj.total_xp = new_player["total_xp"]
        player_obj.missions_completed = new_player["missions_completed"]
        player_obj.list_missions_completed = new_player["list_missions_completed"]

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

        for player in players:
            if player["name"] == player_obj.name:
                player["level"] = player_obj.level
                player["xp"] = player_obj.xp
                player["total_xp"] = player_obj.total_xp
                player["missions_completed"] = player_obj.missions_completed
                player["list_missions_completed"] = player_obj.list_missions_completed

                break

        with open(self.players_file, "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4, ensure_ascii=False)

    def find_player(self, name):
            players = self.load_players()
            player_obj = Player(name)
    
            for player in players:
                if player["name"] == name:
                    player_obj.level = player["level"]
                    player_obj.xp = player["xp"]
                    player_obj.total_xp = player["total_xp"]
                    player_obj.missions_completed = player["missions_completed"]
                    player_obj.list_missions_completed = player["list_missions_completed"]
    
                    return player_obj
    
            return None
