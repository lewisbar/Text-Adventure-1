from items import Gold

class Enemy():
	def __init__(self, name, hp, damage, item):
		self.name = name
		self.hp = hp
		self.damage = damage
		self.item = item
		
	def is_alive(self):
		return self.hp > 0

class GiantSpider(Enemy):
	def __init__(self):
		super().__init__(
			name='Giant Spider',
			hp=9,
			damage=2,
			item=Gold(11)
		)

class Ogre(Enemy):
	def __init__(self):
		super().__init__(
			name='Ogre',
			hp=30,
			damage=15,
			item=Gold(50)
		)
