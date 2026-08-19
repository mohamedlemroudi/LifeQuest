import json
from models.Mission import Mission
from storage.JsonStorage import JsonStorage

class MissionManager:
    def __init__(self):
        self.storage = JsonStorage("missions.json")
        self.list_missions = []

    def load_missions(self):
        missions = self.storage.load()
        self.list_missions = []
        
        for mission in missions:

            self.list_missions.append(Mission.from_dict(mission))
                
        return self.list_missions


    def get_available_missions(self, player_missions_list):
            return [
                mission
                for mission in self.list_missions
                if mission.id not in player_missions_list
            ]

    def get_mission_by_position(self, mission_number, missions_completed):
        available_missions = self.get_available_missions(missions_completed)
        
        if 1 <= mission_number <= len(available_missions):
            return available_missions[mission_number - 1]
        else:
            return None