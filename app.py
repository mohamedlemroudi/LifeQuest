def show_player(player):
    print("Jugador: " + player["name"])
    print("Nivel: " + str(player["level"]))
    print("XP: " + str(player["xp"]))
    print("Niveles ganados: " + str(player["levels_gained"]))

def level_up(player):
    player["levels_gained"] = player["xp"] // 100
    player["level"] += player["levels_gained"]
    player["xp"] -= 100 * (player["levels_gained"])

def gain_xp(player, amount):
    player["xp"] += amount
    return player["xp"]

def show_mission(missions_list):
    for i, mission in enumerate(missions_list, start=1):
        print(f"{i}. {mission['name']}")

    print("0. Salir")

def ask_mission(player, missions_list):
    continuar = True
    player["levels_gained"] = 0
    
    while continuar:
        show_mission(missions_list)

        try:
            mission_number = int(input("Elige una misión: "))
            
            if 1 <= mission_number <= len(missions_list):
                mission_selected = missions_list[mission_number - 1] 
                print("Has completado:" + mission_selected["name"])
                print("Has ganado " + str(mission_selected["xp"]) + " XP.")

                missions_list.remove(mission_selected)
    
                gain_xp(player, mission_selected["xp"])
    
            elif mission_number == 0:
                print("Saliendo del juego.")
                continuar = False
    
            else:
                print("No existe esa misión.")

        except ValueError:
            print("Respuesta no válida.")

    if player["xp"] >= 100:
        level_up(player)
        
        print("¡Felicidades! Has subido al nivel " + str(player["level"]) + ".")
        print("¡Has ganado " + str(player["levels_gained"]) + " niveles!")


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