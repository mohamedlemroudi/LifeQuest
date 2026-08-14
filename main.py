from Game import Game
from Player import Player
from Mission import Mission


missions_list = [
    Mission("Estudiar Python", 50, "easy"),
    Mission("Hacer ejercicio", 30, "medium"),
    Mission("Leer 20 páginas", 100, "difficult"),
    Mission("Meditar", 175, "difficult")
]

missions_data_list = [{"name": "Estudiar Python", "xp_reward": 50, "difficulty": "easy"},
{"name": "Hacer ejercicio", "xp_reward": 30, "difficulty": "medium"},
{"name": "Leer 20 páginas", "xp_reward": 100, "difficulty": "difficult"},
{"name": "Meditar", "xp_reward": 175, "difficulty": "difficult"}]


player_1 = Player("Mohamed")

player_2 = Player("Pep")

# player_2 = Player("Pep")

game = Game(player_2, missions_list)

# game.save_mission(missions_data_list)

game.start()