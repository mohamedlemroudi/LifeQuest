from Game import Game
from Player import Player
from Mission import Mission

def show_player(player):
    print("Jugador: " + player.name)
    print("Nivel: " + str(player.level))
    print("XP: " + str(player.xp))
    print("Misiones completadas: " + str(player.missions_completed))
    print("XP total: " + str(player.total_xp))

def show_stats(player):
    print(f"Jugador: {player.name}")
    print(f"Nivel: {player.level}")
    print(f"XP actual: {player.xp}")
    print(f"XP total: {player.total_xp}")
    print(f"Misiones completadas: {player.missions_completed}")

    if player.missions_completed > 0:
        average_xp = player.total_xp / player.missions_completed
    else:
        average_xp = 0

    print(f"XP media por misión: {average_xp}")


def show_menu():
    print("====================")
    print("     LIFEQUEST")
    print("====================")
    print("1. Ver jugador")
    print("2. Completar misión")
    print("3. Ver estadísticas")
    print("0. Salir")


missions_list = [
    Mission("Estudiar Python", 50, "easy"),
    Mission("Hacer ejercicio", 30, "medium"),
    Mission("Leer 20 páginas", 100, "difficult"),
    Mission("Meditar", 175, "difficult")
]


player_1 = Player("Mohamed")

game = Game(player_1, missions_list)

while True:
    show_menu()
    choice = input("Elige una opción: ")

    if choice == "1":
        show_player(player_1)
    elif choice == "2":
        game.ask_mission()
    elif choice == "3":
        show_stats(player_1)
    elif choice == "0":
        print("Saliendo del juego.")
        break
    else:
        print("Opción no válida. Por favor, elige otra opción.")