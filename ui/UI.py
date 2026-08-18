
class UI:
    def __init__(self):
        pass

    def show_initial_menu(self):
        print("====================")
        print("     LIFEQUEST")
        print("====================")
        print("1. Iniciar sesión")
        print("2. Crear jugador")
        print("0. Salir")

    def ask_initial_choice(self):
        while True:
            try:
                initial_choice = int(input("Elige una opción: "))
                if (initial_choice in (1,2, 0)):
                    return initial_choice
                else:
                    print("No existe esta opcion.")
            except ValueError:
                print("Respuesta no válida.")

    def show_menu(self):
        print("====================")
        print("     LIFEQUEST")
        print("====================")
        print("1. Ver jugador")
        print("2. Completar misión")
        print("3. Ver estadísticas")
        print("0. Salir")

    def show_player(self, player):
        print("Jugador: " + player.name)
        print("Nivel: " + str(player.level))
        print("XP: " + str(player.xp))
        print("Misiones completadas: " + str(player.missions_completed))
        print("XP total: " + str(player.total_xp))

    def show_stats(self, player):
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

    def show_missions(self, missions):
        for position, mission in enumerate(missions, 1):
            print(
                f"{position}. {mission.name} | "
                f"{mission.difficulty} | "
                f"+{mission.calculate_reward()} XP"
            )

        print("0. Volver al menú principal.")


    def ask_missions(self):
        try:
            return int(input("Elige una misión: "))

        except ValueError:
            print("Respuesta no válida.")