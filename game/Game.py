from managers.PlayerManager import PlayerManager
from managers.MissionManager import MissionManager
from ui.UI import UI

class Game:
    def __init__(self):
        self.player = ""
        self.missions_list = []
        self.ui = UI()

    def mission_completed(self, selected_mission):
        reward = selected_mission.calculate_reward()

        self.player.complete_mission(selected_mission.id, reward)

        print(f"Has completado: {selected_mission.name}")
        print(f"Has ganado {reward} XP.")


    def get_available_missions(self):
        return [
            mission
            for mission in self.missions_list
            if mission.id not in self.player.list_missions_completed
        ]

    def get_mission_by_position(self, mission_number):
        available_missions = self.get_available_missions()
        
        if 1 <= mission_number <= len(available_missions):
            selected_mission = available_missions[mission_number - 1]
            
            self.mission_completed(selected_mission)
        else:
            print("No existe esa misión.")


    def ask_mission(self):
        continuar = True
        
        while continuar:
            available_missions = self.get_available_missions()

            self.ui.show_missions(available_missions)

            mission_number = self.ui.ask_missions()

            if (mission_number > 0):
                self.get_mission_by_position(mission_number)
            else:
                continuar = False

        
    def show_initial_menu(self):
        print("====================")
        print("     LIFEQUEST")
        print("====================")
        print("1. Iniciar sesión")
        print("2. Crear jugador")
        print("0. Salir")

    def options_menu(self, player_manager):
        missions_manager = MissionManager()
        self.missions_list = missions_manager.create_missions()

        while True:
            self.ui.show_menu()
            choice = input("Elige una opción: ")

            if choice == "1":
                self.ui.show_player(self.player)
            elif choice == "2":
                self.ask_mission()
            elif choice == "3":
                self.ui.show_stats(self.player)
            elif choice == "0":
                player_manager.update_player(self.player)
                print("Saliendo del juego.")
                break
            else:
                print("Opción no válida. Por favor, elige otra opción.")

    def ask_initial_choice(self):
        while True:
            try:
                self.show_initial_menu()
                initial_choice = int(input("Elige una opción: "))
                if (initial_choice in (1,2, 0)):
                    return initial_choice
                else:
                    print("No existe esta opcion.")
            except ValueError:
                print("Respuesta no válida.")


    def login(self):
        player_manager = PlayerManager()
        player_name = input("Introduce el nombre del jugadora: ")
        self.player = player_manager.find_player(player_name)

        if self.player is not None:
            print("Login CORRECT!")
            self.options_menu(player_manager)
        else:
            print("Login INCORRECT!")

    def signin(self):
        player_manager = PlayerManager()
        player_name = input("Introduce el nombre del jugador: ")
        self.player = player_manager.find_player(player_name)
        
        if self.player is None:
            self.player = player_manager.create_player(player_name)
            print(f"Se ha creado el jugador {self.player.name}")
        else:
            print("El jugador ja existe.")

    def start(self):
        while True:
            initial_choice = self.ask_initial_choice()
            if(initial_choice == 1):
                self.login()
                
            elif(initial_choice == 2):
                self.signin()

            elif (initial_choice == 0):
                print("Salir del programa.")
                break     