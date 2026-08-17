class Mission:
    def __init__(self, id, name, xp_reward, difficulty):
        self.id = id
        self.name = name
        self.xp_reward = xp_reward
        self.difficulty = difficulty

    def calculate_reward(self):

        multiplier = {
            "easy": 1,
            "medium": 1.5,
            "difficult": 2
        }

        return self.xp_reward * multiplier[self.difficulty]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "xp_reward": self.xp_reward,
            "difficulty": self.difficulty
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["xp_reward"],
            data["difficulty"]
        )
