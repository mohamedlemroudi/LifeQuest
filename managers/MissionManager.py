import json
from pathlib import Path
from models.Mission import Mission

class MissionManager:
    BASE_DIR = Path(__file__).resolve().parent.parent
    missions_file = BASE_DIR / "data" / "missions.json"
    
    def __init__(self):
        pass

    def load_missions(self):
        try:
            with open(self.missions_file, "r", encoding="utf-8") as file:
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