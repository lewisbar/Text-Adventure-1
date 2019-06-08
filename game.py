from world import World
import tiles
from player import Player
from items import *
from action import Action
from narrate import narrate, list_up

class Game():
	def play(self):
		# Prepare
		self.prepare_new_game()
		
		# Game loop
		while self.is_playing:
			# List up possible actions
			actions = self.possible_actions_at(self.player.x_position, self.player.y_position)
			list_up(*[str(a) for a in actions], char_delay=0.005, line_delay=0.1)
			
			# Add secret cheat actions
			actions.append(self.show_map_outline_action)
			actions.append(self.show_map_reveal_action)
			
			# Get input
			inpt = input().lower()
			
			# Execute selected action
			for a in actions:
				if inpt == a.hotkey:
					a.method(self)
					break
			else:
				print('')
			
			# Handle death
			if not self.player.is_alive():
				inpt = input('Try again? (y/n)').lower()
				if inpt == 'y':
					self.prepare_new_game()
				else:
					narrate('\nGoodbye! See you next time.')
					self.is_playing = False
		
	def prepare_new_game(self):
		self.world = World()
		self.player = Player(
			hp=80, 
			weapon=Fists(), 
			gold=0
		)
		self.move_to(2, 8)
		self.is_playing = True
		
	def possible_actions_at(self, x, y):
		actions = []
		directions = self.world.possible_directions_from(x, y)
		if 'north' in directions:
			actions.append(self.move_north_action)
		if 'south' in directions:
			actions.append(self.move_south_action)
		if 'west' in directions:
			actions.append(self.move_west_action)
		if 'east' in directions:
			actions.append(self.move_east_action)
		room = self.world._map[y][x]
		if isinstance(room, tiles.EnemyRoom) and room.enemy.is_alive():
			actions.append(self.attack_action)
		actions.append(self.show_inventory_action)
		actions.append(self.show_map_explore_action)
		actions.append(self.quit_action)
		return actions

	def show_inventory(self):
		list_up(
*'''
 
INVENTORY:
Health: {}
Weapon: {}
Damage: {}
Gold: {}
 
'''
.format(self.player.hp, self.player.weapon.name, self.player.weapon.damage, self.player.gold)
.split('\n'))
	
	# Moving
	def move_north(self):
		x, y = self.player.x_position, self.player.y_position
		y -= 1
		self.move_to(x, y)
	
	def move_south(self):
		x, y = self.player.x_position, self.player.y_position
		y += 1
		self.move_to(x, y)
	
	def move_west(self):
		x, y = self.player.x_position, self.player.y_position
		x -= 1
		self.move_to(x, y)
	
	def move_east(self):
		x, y = self.player.x_position, self.player.y_position
		x += 1
		self.move_to(x, y)
	
	def move_to(self, x, y):
		self.player.x_position = x
		self.player.y_position = y
		room = self.world._map[y][x]
		room.is_explored = True
		narrate(room.intro_text())
		narrate(room.modify_player(self.player))
		if isinstance(room, tiles.Exit):
			if input('\nPlay again? (y/n)').lower() == 'y':
				self.prepare_new_game()
			else:
				narrate('\nGoodbye! See you next time.')
				self.is_playing = False
			
	# Attacking
	def attack(self):
		room = self.world._map[self.player.y_position][self.player.x_position]
		if isinstance(room, tiles.EnemyRoom):
			room.enemy.hp -= self.player.weapon.damage
			if not room.enemy.is_alive():
				narrate('\nYou kill {} with {}!'.format(room.enemy.name, self.player.weapon.name))
				self.player.add_loot(room.enemy.item)
				narrate('It drops {} gold.\n'.format(room.enemy.item.value))
			else:
				narrate('\nYou deal {0} damage to {1} with {2}. {1} has {3} HP left.\n'.format(self.player.weapon.damage, room.enemy.name, self.player.weapon.name, room.enemy.hp))
				narrate(room.modify_player(self.player))
	
	# Quit game
	def quit(self):
		inpt = input('\nAre you sure you want to quit? All progress will be lost. Quit game? (y/n)')
		if inpt.lower() == 'y':
			narrate('\nGoodbye! See you next time.')
			self.is_playing = False
		else:
			print('')
	
	# Map
	def show_map_explore(self):
		# Default map
		print(self.world.map_str(self.player.x_position, self.player.y_position))
	
	def show_map_outline(self):
		# Cheat: Shows all walls
		print(self.world.map_str(self.player.x_position, self.player.y_position, mode='outline'))
	
	def show_map_reveal(self):
		# Cheat: Shows everything
		print(self.world.map_str(self.player.x_position, self.player.y_position, mode='reveal'))
			
	# Actions
	show_inventory_action = Action(
		name='Inventory',
		hotkey='i',
		method=show_inventory
	)
	move_north_action = Action(
		name='Move north',
		hotkey='n',
		method=move_north
	)
	move_south_action = Action(
		name='Move south',
		hotkey='s',
		method=move_south
	)
	move_west_action = Action(
		name='Move west',
		hotkey='w',
		method=move_west
	)
	move_east_action = Action(
		name='Move east',
		hotkey='e',
		method=move_east
	)
	attack_action = Action(
		name='Attack',
		hotkey='a',
		method=attack
	)
	quit_action = Action(
		name='Quit',
		hotkey='q',
		method=quit
	)
	show_map_explore_action = Action(
		name='Map',
		hotkey='m',
		method=show_map_explore
	)
	show_map_outline_action = Action(
		name='Map Outline',
		hotkey='mo',
		method=show_map_outline
	)
	show_map_reveal_action = Action(
		name='Map',
		hotkey='mr',
		method=show_map_reveal
	)

if __name__ == '__main__':
	Game().play()
		
