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

        self.ui.show_mission_completed(selected_mission.name, reward)


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

    def options_menu(self, player_manager):
        missions_manager = MissionManager()
        self.missions_list = missions_manager.create_missions()

        while True:
            self.ui.show_menu()
            choice = self.ui.ask_options_menu()

            if choice == 1:
                self.ui.show_player(self.player)

            elif choice == 2:
                self.ask_mission()
                
            elif choice == 3:
                self.ui.show_stats(self.player)
                
            elif choice == 0:
                player_manager.update_player(self.player)
                break

    def login(self):
        player_manager = PlayerManager()
        player_name = self.ui.ask_player_name()
        self.player = player_manager.find_player(player_name)

        if self.player is not None:
            self.ui.show_result_login(True)
            self.options_menu(player_manager)
        else:
            self.ui.show_result_login(False)

    def signin(self):
        player_manager = PlayerManager()
        player_name = self.ui.ask_player_name()
        self.player = player_manager.find_player(player_name)
        
        if self.player is None:
            self.player = player_manager.create_player(player_name)
            self.ui.show_result_singin(True)
        else:
            self.ui.show_result_singin(False)

    def start(self):
        while True:
            self.ui.show_initial_menu()
            initial_choice = self.ui.ask_initial_choice()
            if(initial_choice == 1):
                self.login()
                
            elif(initial_choice == 2):
                self.signin()

            elif (initial_choice == 0):
                break     