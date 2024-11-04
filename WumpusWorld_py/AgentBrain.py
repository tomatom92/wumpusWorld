from collections import deque
from AgentAction import AgentAction
from Variables import Variables

class AgentBrain:

	def __init__(self):
		self.current_num_moves = 0
		self.previous_moves = deque()
		self._next_move = None

	@property
	def next_move(self):
		return self._next_move

	@next_move.setter
	def next_move(self, m):
		if m == AgentAction.quit:
			exit(0)
		elif self._next_move != None:
			print("Trouble adding move, only allowed to add 1 at a time")
		else:
			self._next_move = m

	def get_opposite_action(self, a:AgentAction):
		if a == AgentAction.move_down:
			return AgentAction.move_up
		elif a == AgentAction.move_up:
			return AgentAction.move_down
		elif a == AgentAction.move_left:
			return AgentAction.move_right
		elif a == AgentAction.move_right:
			return AgentAction.move_left
		return AgentAction.do_nothing
	
	#For wumpus world, we do one move at a time
	def get_next_move(self, visible_map):
		if Variables.GAME_PLAY_TYPE == Variables.GamePlayType.KEYBOARD:
			if self._next_move == None:
				return AgentAction.do_nothing
			else:
				tmp = self._next_move
				self._next_move = None
				return tmp
		elif Variables.GAME_PLAY_TYPE == Variables.GamePlayType.RANDOM:
			#Just does random things - then undo them
			if Variables.RANDOMIZE_PLAYER:
				#We don't know where we started
				if self.current_num_moves < Variables.NUM_RANDOM_MOVES:
					self.current_num_moves+=1
					return self.random_move(visible_map)
				return AgentAction.declare_victory
			else:
				#We started at the first, and can work our way back there
				if Variables.last_action_worked == False:
					if self.previous_moves.size() > 0:
						self.previous_moves.pop()
				if self.current_num_moves < Variables.NUM_RANDOM_MOVES-1:
					self.current_num_moves+=1
					a = self.random_move(visible_map)
					if a == AgentAction.pickup_something:
						#we are done, and can exit the map
						self.current_num_moves = Variables.NUM_RANDOM_MOVES-1
						return a
					else:
						self.previous_moves.append(a)
						return a
				elif self.current_num_moves < Variables.NUM_RANDOM_MOVES and len(self.previous_moves) > 0:
					self.previous_moves = AgentAction.remove_back_and_forth(self.previous_moves)
					if len(self.previous_moves) == 0:
						return AgentAction.declare_victory
					a = self.previous_moves.pop()
					b = self.get_opposite_action(a)
					return b
				else:
					return AgentAction.declare_victory
		else:
			return self.brain(visible_map)

	@staticmethod
	def random_move(visible_map):
		return AgentAction.random_action(visible_map)

	@staticmethod
	def brain(visible_map):
		#TODO: Put More Methods Here As You Go
		return AgentBrain.get_out_alive(visible_map)

	@staticmethod
	def get_out_alive(self, visible_map):
		#Possible things to add to your moves
#		self.next_move = AgentAction.do_nothing
#		self.next_move = AgentAction.move_down
#		self.next_move = AgentAction.move_up
#		self.next_move = AgentAction.move_up
#		self.next_move = AgentAction.move_left
#		self.next_move = AgentAction.pickup_something
#		self.next_move = AgentAction.declare_victory

#		self.next_move = AgentAction.shoot_arrow_north
#		self.next_move = AgentAction.shoot_arrow_south
#		self.next_move = AgentAction.shoot_arrow_east
#		self.next_move = AgentAction.shoot_arrow_west
#		self.next_move = AgentAction.quit
		return AgentAction.declare_victory
