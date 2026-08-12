def show_player(player):
    print("Jugador: " + player["name"])
    print("Nivel: " + str(player["level"]))
    print("XP: " + str(player["xp"]))
    print("Misiones completadas: " + str(player["missions_completed"]))
    print("XP total: " + str(player["total_xp"]))

def show_stats(player):
    print("Jugador: " + player["name"])
    print("Nivell: " + str(player["level"]))
    print("XP actual: " + str(player["xp"]))
    print("XP total: " + str(player["total_xp"]))
    print("Misiones completadas: " + str(player["missions_completed"]))

    if player["missions_completed"] > 0:
        average_xp = player["total_xp"] / player["missions_completed"]
    else:
        average_xp = 0

    print("XP media por misión: " + str(average_xp))

def calculate_levels_gained(player):
    return player["xp"] // 100


def gain_xp(player, amount):
    player["xp"] += amount
    player["total_xp"] += amount


def show_mission(missions_list):
    position = 1
    for mission in missions_list:
        if not mission["completed"]:
            print(f"{position}. {mission['name']} | {mission['difficulty']} | +{mission['xp']} XP")
            position += 1

    print("0. Salir")

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

    gain_xp(player, reward)

    player["missions_completed"] += 1
    
    check_level_up(player)

def check_level_up(player):
    if player["xp"] >= 100:
        levels_gained = calculate_levels_gained(player)
        player["level"] += levels_gained
        player["xp"] -= 100 * levels_gained
        
        print("¡Felicidades! Has subido al nivel " + str(player["level"]) + ".")
        print("¡Has ganado " + str(levels_gained) + " niveles!")


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
                print("Saliendo del juego.")
                continuar = False
                show_stats(player)
    
            else:
                print("No existe esa misión.")

        except ValueError:
            print("Respuesta no válida.")


player = {
    "name": input("Enter your name: "),
    "level": 1,
    "xp": 0,
    "missions_completed": 0,
    "total_xp": 0
}

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

show_player(player)

ask_mission(player, missions_list)

show_player(player)