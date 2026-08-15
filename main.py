from Game import Game
from Player import Player
from Mission import Mission


missions_list = [
    Mission("Estudiar Python", 50, "easy"),
    Mission("Hacer ejercicio", 30, "medium"),
    Mission("Leer 20 páginas", 100, "difficult"),
    Mission("Meditar", 175, "difficult")
]

player_1 = Player("Mohamed")

player_2 = Player("Pep")


game = Game(player_1, missions_list)

game.start()