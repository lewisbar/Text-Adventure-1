# import world
from items import Weapon, Gold

class Player():
	def __init__(self, hp, weapon, gold):
		self.hp = hp
		self.weapon = weapon
		self.gold = gold
		self.x_position = 0
		self.y_position = 0

	def is_alive(self):
		return self.hp > 0

	def add_loot(self, item):
		if isinstance(item, Weapon):
			if item.damage > self.weapon.damage:
				self.weapon = item
		elif isinstance(item, Gold):
			self.gold += item.value
