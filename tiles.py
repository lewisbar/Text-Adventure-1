import items, enemies


class MapTile():
	# Abstract. Subclasses must implement intro_text(self) and modify_player(self, player).
	def __init__(self):
		self.is_explored = False

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, player):
		raise NotImplementedError()
	
	def short_name(self):
		raise NotImplementedError()


class StartingRoom(MapTile):
	def intro_text(self):
		return '''
You find yourself if a cave with a flickering torch on the wall.
You can make out four paths, each equally as dark and foreboding.
		'''

	def modify_player(self, player):
		# Room has no effect on player
		pass
	
	def short_name(self):
		return 'START'


class LootRoom(MapTile):
	# Abstract. Subclasses must implement intro_text(self) and short_name(self).
	def __init__(self, item):
		self.item = item
		super().__init__()

	#def add_loot(self, player):
	#	player.inventory.append(self.item)

	def modify_player(self, player):
		if self.item:
			itm = self.item
			player.add_loot(itm)
			self.item = None
			# return 'Added {} to inventory.\n'.format(itm.name)



class EnemyRoom(MapTile):
	# Abstract. Subclasses must implement intro_text(self) and short_name(self).
	def __init__(self, enemy):
		self.enemy = enemy
		super().__init__()

	def modify_player(self, player):
		if self.enemy.is_alive():
			player.hp -= self.enemy.damage
			if player.is_alive():
				return '{} deals {} damage to you. You have {} HP remaining.\n'.format(self.enemy.name, self.enemy.damage, player.hp)
			else:
				return ('{} killed you!'.format(self.enemy.name))


class EmptyCavePath(MapTile):
	def intro_text(self):
		return '''
Another unremarkable part of the cave. You must forge onwards.
		'''

	def modify_player(self, player):
		# Room has no action on player.
		pass
	
	def short_name(self):
		return 'Empty'


class GiantSpiderRoom(EnemyRoom):
	def __init__(self):
		super().__init__(enemies.GiantSpider())

	def intro_text(self):
		if self.enemy.is_alive():
			return '''
A giant spider jumps down from its web in front of you!
			'''
		else:
			return '''
The corpse of a dead spider rots on the ground.
			'''
		
	def short_name(self):
		return 'Spider'


class OgreRoom(EnemyRoom):
	def __init__(self):
		super().__init__(enemies.Ogre())
	
	def intro_text(self):
		if self.enemy.is_alive():
			return '''
You find yourself in front of an enormous Ogre. It grunts furiously and raises its gigantic club to crush you.
			'''
		else:
			return '''
Half the ground is covered with the huge corpse of an Ogre.
			'''
	
	def short_name(self):
		return 'Ogre'


class FindRockRoom(LootRoom):
	def __init__(self):
		super().__init__(items.Rock())
	
	def intro_text(self):
		if self.item:
			return '''
Desperately searching for some kind of weapon in this dangerous place, you pick up a rock from the ground.
			'''
		else:
			return '\nHaven\'t you already been here? All these cave rooms look so similar.\n'
	
	def short_name(self):
		return 'Rock'


class FindDaggerRoom(LootRoom):
	def __init__(self):
		super().__init__(items.Dagger())

	def intro_text(self):
		if self.item:
			return '''
You notice something shiny in the corner.
It's a dagger! You pick it up.
			'''
		else:
			return '\nHaven\'t you already been here? All these cave rooms look so similar.\n'
	
	def short_name(self):
		return 'Dagger'


class FindGoldRoom(LootRoom):
	def __init__(self):
		super().__init__(items.Gold(5))
	
	def intro_text(self):
		if self.item:
			return '\nYou find a rusty chest with {} gold in it!\n'.format(self.item.value)
		else:
			return '\nYou see an open chest. It\'s empty.\n'
	
	def short_name(self):
		return 'Gold'
		

class Exit(MapTile):
	def __init__(self):
		super().__init__()
		
	def intro_text(self):
		return '''
You see light ahead. Barely able to believe, you stumble into the warm daylight. You made it out alive!'''
	
	def modify_player(self, player):
		player.is_playing = False
		return 'You reached {} points.'.format(player.gold + player.hp)
	
	def short_name(self):
		return 'EXIT'
