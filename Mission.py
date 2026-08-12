class Mission:
    def __init__(self, name, xp_reward, difficulty, completed=False):
        self.name = name
        self.xp_reward = xp_reward
        self.difficulty = difficulty
        self.completed = completed

    def calculate_reward(self):

        multiplier = {
            "easy": 1,
            "medium": 1.5,
            "difficult": 2
        }

        return self.xp_reward * multiplier[self.difficulty]

    def complete(self):
        self.completed = True
