from SaveManager import SaveManager

class Game:
    def __init__(self, player, missions_list):
        self.player = player
        self.missions_list = missions_list

    def show_menu(self):
        print("====================")
        print("     LIFEQUEST")
        print("====================")
        print("1. Ver jugador")
        print("2. Completar misión")
        print("3. Ver estadísticas")
        print("0. Salir")

    def show_stats(self):
        print(f"Jugador: {self.player.name}")
        print(f"Nivel: {self.player.level}")
        print(f"XP actual: {self.player.xp}")
        print(f"XP total: {self.player.total_xp}")
        print(f"Misiones completadas: {self.player.missions_completed}")

        if self.player.missions_completed > 0:
            average_xp = self.player.total_xp / self.player.missions_completed
        else:
            average_xp = 0

        print(f"XP media por misión: {average_xp}")


    def show_mission(self):
        position = 1
        for mission in self.missions_list:
            if not mission.completed:
                print(f"{position}. {mission.name} | {mission.difficulty} | +{mission.xp_reward} XP")
                position += 1

        print("0. Volver al menú principal.")

    def mission_completed(self, selected_mission):
        reward = selected_mission.calculate_reward()

        selected_mission.complete()

        print(f"Has completado: {selected_mission.name}")
        print(f"Has ganado {reward} XP.")

        self.player.complete_mission(reward)

    def get_available_missions(self):
        return [
            mission
            for mission in self.missions_list
            if not mission.completed
        ]


    def ask_mission(self):
        continuar = True
        
        while continuar:
            self.show_mission()

            try:
                mission_number = int(input("Elige una misión: "))

                available_missions = self.get_available_missions()

                if 1 <= mission_number <= len(available_missions):
                    selected_mission = available_missions[mission_number - 1]
                    
                    self.mission_completed(selected_mission)
        
                elif mission_number == 0:
                    print("Volviendo al menú principal.")
                    continuar = False
        
                else:
                    print("No existe esa misión.")

            except ValueError:
                print("Respuesta no válida.")


    def start(self):
        while True:
            save_player = SaveManager(self.player)
            save_player.find_player()
            self.show_menu()
            choice = input("Elige una opción: ")

            if choice == "1":
                self.player.show_player()
            elif choice == "2":
                self.ask_mission()
            elif choice == "3":
                self.show_stats()
            elif choice == "0":
                save_player.update_player()
                print("Saliendo del juego.")
                break
            else:
                print("Opción no válida. Por favor, elige otra opción.")
