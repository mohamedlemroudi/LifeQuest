import json
from pathlib import Path
from models.Mission import Mission
from storage.JsonStorage import JsonStorage

class MissionManager:
    def __init__(self):
        self.storage = JsonStorage("missions.json")

    def create_missions(self):
        missions = self.storage.load()
        list_missions = []
        
        for mission in missions:

            list_missions.append(Mission.from_dict(mission))
                
        return list_missions