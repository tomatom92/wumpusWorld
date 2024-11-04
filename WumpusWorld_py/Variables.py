from enum import Enum

class Variables:
	GamePlayType = Enum('GamePlayType', ['KEYBOARD','RANDOM','BRAIN'])
	WorldType = Enum("WorldType", ['ONLY_GOLD', 'GOLD_IN_PITS', 'GOLD_UNDER_WUMPUS'])

Variables.GAME_PLAY_TYPE = Variables.GamePlayType.RANDOM
Variables.SLEEP_TIME = 50
	
Variables.NUM_GAMES = 20
Variables.NUM_RANDOM_MOVES = 20
Variables.AUTO_ADVANCE_ROUNDS = True

Variables.RANDOMIZE_PLAYER = False
Variables.REMOVE_DARKNESS = False
Variables.MAKE_WUMPUS_GUARD_GOLD = False
	
Variables.ADD_PITS = True
Variables.ADD_WUMPUS = True
Variables.ADD_WALLS = True

Variables.last_action_worked = True
Variables.num_games_played = 0

Variables.CHEATMODE_ON = False