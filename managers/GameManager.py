class GameManager:
    def __init__(self, game):
        self.game = game

    def start(self):
        while True:
            self.game.ui.show_initial_menu()
            initial_choice = self.game.ui.ask_initial_choice()

            if(initial_choice == 1):
                self.game.login()
                
            elif(initial_choice == 2):
                self.game.signin()

            elif (initial_choice == 0):
                break     

            
