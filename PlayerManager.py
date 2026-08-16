import json

class PlayerManager:

    def __init__(self, player):
        self.player = player   
     

    def create_player(self, players):
        new_player = {
            "name":self.player.name,
            "level":1,
            "xp": 0,
            "total_xp": 0,
            "missions_completed": 0,
            "list_missions_completed": []
        }

        players.append(new_player)

        with open("players.json", "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4, ensure_ascii=False)

        # Cargar los valores del nuevo jugador en el objeto
        self.player.level = new_player["level"]
        self.player.xp = new_player["xp"]
        self.player.total_xp = new_player["total_xp"]
        self.player.missions_completed = new_player["missions_completed"]
        self.player.list_missions_completed = new_player["list_missions_completed"]

        return new_player
    

    def load_players(self):
        try:
            with open("players.json", "r", encoding="utf-8") as file:
                players = json.load(file)

            # Si el JSON todavía tiene un solo jugador
            # lo convertimos automáticamente en lista
            if isinstance(players, dict):
                players = [players]

        except (FileNotFoundError, json.JSONDecodeError):
            players = []

        return players


    def update_player(self):
        players = self.load_players()

        for player in players:
            if player["name"] == self.player.name:
                player["level"] = self.player.level
                player["xp"] = self.player.xp
                player["total_xp"] = self.player.total_xp
                player["missions_completed"] = self.player.missions_completed
                player["list_missions_completed"] = self.player.list_missions_completed

                break

        with open("players.json", "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4, ensure_ascii=False)


    def find_player(self):
        players = self.load_players()

        for player in players:
            if player["name"] == self.player.name:
                self.player.level = player["level"]
                self.player.xp = player["xp"]
                self.player.total_xp = player["total_xp"]
                self.player.missions_completed = player["missions_completed"]
                self.player.list_missions_completed = player["list_missions_completed"]

                return player

        return self.create_player(players)
