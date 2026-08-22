from datetime import datetime

class Mission:
    def __init__(self, id, name, xp_reward, difficulty, date_limit_string):
        self.id = id
        self.name = name
        self.xp_reward = xp_reward
        self.difficulty = difficulty
        self.days_left = self.get_days_left(date_limit_string)


    def get_days_left(self, date_limit_string):
        format = "%d/%m/%Y %H:%M:%S"
        date_limit_obj = datetime.strptime(date_limit_string, format)
        
        date_diff = date_limit_obj - datetime.now()

        return date_diff.days
        

    def calculate_reward(self):

        multiplier = {
            "easy": 1,
            "medium": 1.5,
            "difficult": 2
        }

        return self.xp_reward * multiplier[self.difficulty]

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["name"],
            data["xp_reward"],
            data["difficulty"],
            data["date_limit"]
        )
