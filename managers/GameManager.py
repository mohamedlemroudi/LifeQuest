class GameManager:
    def __init__(self, game):
        self.game = game

    def start(self):
        while True:
            initial_choice = self.game.ask_options_intial_menu()
            if(initial_choice == 1):
                self.game.login()
                
            elif(initial_choice == 2):
                self.game.signin()

            elif (initial_choice == 0):
                break     

            
