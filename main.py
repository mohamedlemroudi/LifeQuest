from Game import Game
from Player import Player
from Mission import Mission


missions_list = [
    Mission(1, "Estudiar Python", 50, "easy"),
    Mission(2, "Hacer ejercicio", 30, "medium"),
    Mission(3, "Leer 20 páginas", 100, "difficult"),
    Mission(4, "Meditar", 175, "difficult")
]

player_1 = Player("Mohamed")

game = Game(player_1, missions_list)

game.start()
