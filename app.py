from Player import Player

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


def show_mission(missions_list):
    position = 1
    for mission in missions_list:
        if not mission["completed"]:
            print(f"{position}. {mission['name']} | {mission['difficulty']} | +{mission['xp']} XP")
            position += 1

    print("0. Volver al menú principal.")

def calculate_reward(mission):
    base_reward = mission["xp"]
    multiplier_difficulty = {
        "easy": 1,
        "medium": 1.5,
        "difficult": 2
    }
    return base_reward * multiplier_difficulty.get(mission["difficulty"], 1)

def mission_completed(player, mission_number, available_missions):
    mission_selected = available_missions[mission_number - 1]

    reward = calculate_reward(mission_selected)

    mission_selected["completed"] = True
    
    print("Has completado:" + mission_selected["name"])
    print("Has ganado " + str(reward) + " XP.")

    player.complete_mission(reward)


def ask_mission(player, missions_list):
    continuar = True
    
    while continuar:
        show_mission(missions_list)

        try:
            mission_number = int(input("Elige una misión: "))

            available_missions = [
                mission
                for mission in missions_list
                if not mission["completed"]
            ]

            if 1 <= mission_number <= len(available_missions):
                mission_completed(player, mission_number, available_missions)
    
            elif mission_number == 0:
                print("Volviendo al menú principal.")
                continuar = False
    
            else:
                print("No existe esa misión.")

        except ValueError:
            print("Respuesta no válida.")

missions_list = [
    {
        "name": "Estudiar Python",
        "xp": 50,
        "difficulty": "easy",
        "completed": False
    },
    {
        "name": "Hacer ejercicio",
        "xp": 30,
        "difficulty": "easy",
        "completed": False
    },
    {
        "name": "Leer 20 páginas",
        "xp": 75,
        "difficulty": "medium",
        "completed": False
    },
    {
        "name": "Meditar",
        "xp": 100,
        "difficulty": "difficult",
        "completed": False
    }
]

player_1 = Player("Mohamed")

while True:
    show_menu()
    choice = input("Elige una opción: ")

    if choice == "1":
        show_player(player_1)
    elif choice == "2":
        ask_mission(player_1, missions_list)
    elif choice == "3":
        show_stats(player_1)
    elif choice == "0":
        print("Saliendo del juego.")
        break
    else:
        print("Opción no válida. Por favor, elige otra opción.")