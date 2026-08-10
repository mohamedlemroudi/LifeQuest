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
    for i, mission in enumerate(missions_list, start=1):
        print(f"{i}. {mission['name']} | {mission['difficulty']} | +{mission['xp']} XP")

    print("0. Salir")


def mission_completed(player, missions_list, mission_number):
    mission_selected = missions_list[mission_number - 1] 
    print("Has completado:" + mission_selected["name"])
    print("Has ganado " + str(mission_selected["xp"]) + " XP.")

    missions_list.remove(mission_selected)

    player["levels_gained"] = 0

    gain_xp(player, mission_selected["xp"])


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
            
            if 1 <= mission_number <= len(missions_list):
                mission_completed(player, missions_list, mission_number)
                check_level_up(player)
    
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
        "difficulty": "easy"
    },
    {
        "name": "Hacer ejercicio",
        "xp": 30,
        "difficulty": "easy"
    },
    {
        "name": "Leer 20 páginas",
        "xp": 75,
        "difficulty": "medium"
    },
    {
        "name": "Meditar",
        "xp": 100,
        "difficulty": "difficult"
    }
]

show_player(player)

ask_mission(player, missions_list)

show_player(player)