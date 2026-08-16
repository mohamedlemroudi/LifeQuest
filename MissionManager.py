import json

class MissionManager:
    def __init__(self):
        pass


    def load_missions(self):
        try:
            with open("missions.json", "r", encoding="utf-8") as file:
                missions = json.load(file)

            if isinstance(missions, dict):
                missions = [missions]

        except (FileNotFoundError, json.JSONDecodeError):
            missions = []

        return missions
                