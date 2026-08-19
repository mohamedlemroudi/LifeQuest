from game.Game import Game
from managers.PlayerManager import PlayerManager
from managers.MissionManager import MissionManager
from ui.UI import UI

player_manager = PlayerManager()
missions_manager = MissionManager()
ui = UI()

game = Game(ui, player_manager, missions_manager)

game.start()
