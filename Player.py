class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.total_xp = 0
        self.missions_completed = 0

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

            print("¡Felicidades! Has subido al nivel " + str(self.level) + ".")
            print("¡Has ganado " + str(levels_gained) + " niveles!")

    def complete_mission(self, reward):
        self.gain_xp(reward)
        self.missions_completed += 1
        self.check_level_up()
