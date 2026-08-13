import json

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.total_xp = 0
        self.missions_completed = 0

        self.save_player()

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

    def complete_mission(self, reward):
        self.gain_xp(reward)
        self.missions_completed += 1
        self.check_level_up()


    def save_player(self):
        new_player = {
            "name":self.name,
            "level":0,
            "xp": 0,
            "total_xp": 0,
            "missions_completed": 0
        }

        players = self.load_players()
        players.append(new_player)

        with open("players.json", "w", encoding="utf-8") as file:
            json.dump(players, file, indent=4, ensure_ascii=False)


    def load_players(self):
        try:
            with open("players.json", "r", encoding="utf-8") as file:
                players = json.load(file)
        except:
            players = []

        return players



