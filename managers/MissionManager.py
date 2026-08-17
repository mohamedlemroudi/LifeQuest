import json
from pathlib import Path
from models.Mission import Mission
from storage.JsonStorage import JsonStorage

class MissionManager:
    BASE_DIR = Path(__file__).resolve().parent.parent
    missions_file = BASE_DIR / "data" / "missions.json"
    
    def __init__(self):
        self.storage = JsonStorage(self.missions_file)

    def create_missions(self):
        missions = self.storage.load()
        list_missions = []
        
        for mission in missions:

            list_missions.append(Mission.from_dict(mission))
                
        return list_missions