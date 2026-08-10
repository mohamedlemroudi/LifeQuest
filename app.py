def show_player(player):
    print("Jugador: " + player["name"])
    print("Nivel: " + str(player["level"]))
    print("XP: " + str(player["xp"]))
    print("Niveles ganados: " + str(player["levels_gained"]))

def level_up(player):
    num_levels = player["xp"] // 100
    player["levels_gained"] = num_levels
    player["level"] += num_levels
    player["xp"] -= 100 * num_levels


def gain_xp(player, amount):
    player["xp"] += amount


def show_mission(missions_list):
    position = 1
    for i, mission in enumerate(missions_list, start=1):
        if not mission["completed"]:
            print(f"{position}. {mission['name']} | {mission['difficulty']} | +{mission['xp']} XP")
            position += 1

    print("0. Salir")


def mission_completed(player, mission_number, available_missions):
    mission_selected = available_missions[mission_number - 1]
    print("Has completado:" + mission_selected["name"])
    print("Has ganado " + str(mission_selected["xp"]) + " XP.")

    mission_selected["completed"] = True

    player["levels_gained"] = 0

    gain_xp(player, mission_selected["xp"])

    check_level_up(player)


def check_level_up(player):
    if player["xp"] >= 100:
        level_up(player)
        
        print("¡Felicidades! Has subido al nivel " + str(player["level"]) + ".")
        print("¡Has ganado " + str(player["levels_gained"]) + " niveles!")


def ask_mission(player, missions_list):
    continuar = True
    player["levels_gained"] = 0
    
    while continuar:
        show_mission(missions_list)

        try:
            mission_number = int(input("Elige una misión: "))

            available_missions = [
                mission
                for mission in missions_list
                if not mission["completed"]
            ]
            
            if 1 <= mission_number <= len(available_missions) and len(available_missions) > 0:
                mission_completed(player, mission_number, available_missions)
    
            elif mission_number == 0:
                print("Saliendo del juego.")
                continuar = False
    
            else:
                print("No existe esa misión.")

        except ValueError:
            print("Respuesta no válida.")


player = {
    "name": input("Enter your name: "),
    "level": 1,
    "xp": 0,
    "levels_gained": 0
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