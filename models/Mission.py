from datetime import datetime

class Mission:
    """Representa una misión dentro del juego LifeQuest."""

    # Constantes de clase
    DATE_FORMAT = "%d/%m/%Y %H:%M:%S"
    DIFFICULTY_MULTIPLIERS = {
        "easy": 1,
        "medium": 1.5,
        "difficult": 2
    }

    def __init__(self, id: int, name: str, xp_reward: int, difficulty: str, date_limit_string: str):
        self.id = id
        self.name = name
        self.xp_reward = xp_reward
        self.difficulty = difficulty.lower()
        self.date_limit_string = date_limit_string
    
    def days_left(self) -> int:
        """Calcula en tiempo real los días restantes antes de que caduque la misión."""
        date_limit_obj = datetime.strptime(self.date_limit_string, self.DATE_FORMAT)
        date_diff = date_limit_obj - datetime.now()

        return max(0,date_diff.days)
        
    def calculate_reward(self) -> float:
        """Calcula la recompensa de XP aplicando el multiplicador según la dificultad."""
        multiplier = self.DIFFICULTY_MULTIPLIERS.get(self.difficulty, 1.0)
        return self.xp_reward * multiplier

    @classmethod
    def from_dict(cls, data):
        """Crea una instancia de Mission a partir de un diccionario (datos de JSON)."""
        return cls(
            data["id"],
            data["name"],
            data["xp_reward"],
            data["difficulty"],
            data["date_limit"]
        )

    def __repr__(self) -> str:
        """Representación en texto del objeto para facilitar la depuración (debugging)."""
        return f"Mission(id={self.id}, name='{self.name}', difficulty='{self.difficulty}')"