from tiles import *

class World():
	def __init__(self):
		self._map = [
			[None,              None,              Exit(),            OgreRoom()       ],
			[FindGoldRoom(),    GiantSpiderRoom(), None,              EmptyCavePath()  ],
			[FindGoldRoom(),    EmptyCavePath(),   FindDaggerRoom(),  EmptyCavePath()  ],
			[None,              GiantSpiderRoom(), None,              GiantSpiderRoom()],
			[FindGoldRoom(),    EmptyCavePath(),   None,              FindGoldRoom()   ],
			[EmptyCavePath(),   None,              FindGoldRoom(),    None             ],
			[EmptyCavePath(),   EmptyCavePath(),   GiantSpiderRoom(), None             ],
			[None,              None,              FindRockRoom(),    FindGoldRoom()   ],
			[None,              FindGoldRoom(),    StartingRoom(),    EmptyCavePath()  ],
			[FindGoldRoom(),    EmptyCavePath(),   EmptyCavePath(),   FindGoldRoom()   ],
		]
	
	def is_valid(self, x, y):
		width = len(self._map[0])
		height = len(self._map)
		return (0 <= x < width) and (0 <= y < height) and (self._map[y][x] != None)
	
	def possible_directions_from(self, x, y):
		directions = []
		if self.is_valid(x, y-1):
			directions.append('north')
		if self.is_valid(x, y+1):
			directions.append('south')
		if self.is_valid(x-1, y):
			directions.append('west')
		if self.is_valid(x+1, y):
			directions.append('east')
		return directions
	
	def __str__(self):
		return self.map_str_explore()
	
	def map_str(self, x=None, y=None, mode='explore'):
		'''
		There are three modes:
		- 'explore': Default mode. Only shows what the player has already explored.
		- 'outline': Cheat. Same as 'explore', but shows all walls.
		- 'reveal': Cheat. Shows the whole map.
		'''
		map_str = '\n'
		for i, row in enumerate(self._map):
			for j, room in enumerate(row):
				if not room:
					if self.has_explored_neighbors(j, i) or mode == 'outline' or mode == 'reveal':
						map_str += '####### '
					else:
						map_str += '??????? '
				else:
					display = room.short_name()
					display = display + ((8-len(display))*' ')
					if i == y and j == x:
						display = 'YOU     '
					elif not room.is_explored and not mode == 'reveal':
						display = '??????? '
					else:
						display = room.short_name()
						display = display + ((8-len(display))*' ')
					map_str += display
			map_str += '\n'
		return map_str
	
	# def map_str_outline(self, x=None, y=None):
		
		
	def has_explored_neighbors(self, x, y):
		for i in range(y-1, y+2):
			for j in range(x-1, x+2):
				if self.is_valid(j, i):
					if self._map[i][j].is_explored:
						return True
		return False
