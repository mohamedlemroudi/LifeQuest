from game.Game import Game
from managers.PlayerManager import PlayerManager
from managers.MissionManager import MissionManager
from managers.GameManager import GameManager
from ui.UI import UI

player_manager = PlayerManager()
missions_manager = MissionManager("missions.json")
ui = UI()

game = Game(ui, player_manager, missions_manager)

game_manager = GameManager(game)

game_manager.start()
