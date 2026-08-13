class Game:
    def __init__(self, player, missions_list):
        self.player = player
        self.missions_list = missions_list

    def show_mission(self):
        position = 1
        for mission in self.missions_list:
            if not mission.completed:
                print(f"{position}. {mission.name} | {mission.difficulty} | +{mission.xp_reward} XP")
                position += 1

        print("0. Volver al menú principal.")

    def mission_completed(self, mission_number, available_missions):
        selected_mission = available_missions[mission_number - 1]

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
                    self.mission_completed(mission_number, available_missions)
        
                elif mission_number == 0:
                    print("Volviendo al menú principal.")
                    continuar = False
        
                else:
                    print("No existe esa misión.")

            except ValueError:
                print("Respuesta no válida.")