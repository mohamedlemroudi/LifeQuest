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

            list_missions.append(Mission.from_dict(mission))
                
        return list_missions