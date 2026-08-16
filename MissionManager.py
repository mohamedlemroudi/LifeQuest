import json
from Mission import Mission

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


    def create_missions(self):
        missions = self.load_missions()
        list_missions = []
        
        for mission in missions:
            mission_obj = Mission(mission["id"], mission["name"], 
                                    mission["xp_reward"], mission["difficulty"])

            list_missions.append(mission_obj)
                

        return list_missions