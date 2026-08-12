class Mission:
    def __init__(self, name, xp_reward, difficulty, completed=False):
        self.name = name
        self.xp_reward = xp_reward
        self.difficulty = difficulty
        self.completed = completed

    