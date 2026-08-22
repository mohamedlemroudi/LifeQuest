from typing import List, Optional
from models.Mission import Mission
from storage.JsonStorage import JsonStorage

class MissionManager:
    """Gestiona la carga, filtrado y ordenación de las misiones del juego."""
    def __init__(self, file_name: str = "missions.json"):
        self.storage = JsonStorage(file_name)
        self.list_missions: List[Mission] = []

    def load_missions(self) -> List[Mission]:
        """
        Carga las misiones desde el archivo JSON transformándolas en objetos Mission.
        Sustituye la lista actual para evitar misiones duplicadas si se vuelve a cargar.
        """
        missions_data = self.storage.load()
        # Usamos List Comprehension para crear los objetos de forma limpia
        self.list_missions = [
            Mission.from_dict(data) for data in missions_data
        ]

        return self.list_missions

    def get_available_missions(self, player_missions_list: List[int]) -> List[Mission]:
        """
        Devuelve la lista de misiones no completadas por el jugador y no caducadas,
        ordenadas por urgencia de fecha límite.
        """
        # Convertimos a set para optimizar las búsquedas "not in" a tiempo constante O(1)
        completed_ids = set(player_missions_list)

        list_available_missions = [
            mission
            for mission in self.list_missions
            if mission.id not in completed_ids
            and mission.days_left() > 0
        ]

        return self.sort_missions(list_available_missions)

    def get_mission_by_position(self, mission_number: int, missions_completed: List[int]) -> Optional[Mission]:
        """
        Obtiene una misión disponible basándose en su número de índice de pantalla (1-indexed).
        Devuelve None si el número introducido está fuera de rango.
        """
        available_missions = self.get_available_missions(missions_completed)
        
        if 1 <= mission_number <= len(available_missions):
            return available_missions[mission_number - 1]
        else:
            return None

    def sort_missions(self, list_missions: List[Mission]) -> List[Mission]:
        """Ordena una lista de misiones de menor a mayor cantidad de días restantes."""
        return sorted(list_missions, key=lambda mission: mission.days_left())