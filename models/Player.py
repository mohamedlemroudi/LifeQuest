class Player:
    def __init__(self, name, level = 0, xp = 0, total_xp = 0, 
                 missions_completed = 0, list_missions_completed = []):
        self.name = name
        self.level = level
        self.xp = xp
        self.total_xp = total_xp
        self.missions_completed = missions_completed
        self.list_missions_completed = list_missions_completed

    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "xp": self.xp,
            "total_xp": self.total_xp,
            "missions_completed": self.missions_completed,
            "list_missions_completed": self.list_missions_completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["level"],
            data["xp"],
            data["total_xp"],
            data["missions_completed"],
            data["list_missions_completed"]
        )

    def show_player(self):
        print("Jugador: " + self.name)
        print("Nivel: " + str(self.level))
        print("XP: " + str(self.xp))
        print("Misiones completadas: " + str(self.missions_completed))
        print("XP total: " + str(self.total_xp))


    def gain_xp(self, amount):
        self.xp += amount
        self.total_xp += amount


    def calculate_levels_gained(self):
        return self.xp // 100


    def check_level_up(self):
        levels_gained = self.calculate_levels_gained()

        if levels_gained > 0:
            self.level += levels_gained
            self.xp -= 100 * levels_gained

            print(f"¡Felicidades! Has subido al nivel {self.level}.")
            print(f"¡Has ganado {levels_gained} niveles!")


    def complete_mission(self, id_mission, reward):
        self.gain_xp(reward)
        self.missions_completed += 1
        self.list_missions_completed.append(id_mission)
        self.check_level_up()
