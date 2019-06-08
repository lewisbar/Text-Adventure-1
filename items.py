class Item():
	"""
	The base class for all items.
	"""
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value
		
	def __str__(self):
		return '{}\n=====\n{}\nValue: {}\n'.format(self.name, self.description, self.value)

class Gold(Item):
	def __init__(self, value):
		# self.amount = amount
		super().__init__(
			name='Gold', 
			description='A round coin with a {} stamped on the front.'.format(value), 
			value=value
		)
			
class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name, description, value)
		
	def __str__(self):
		return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

class Fists(Weapon):
	def __init__(self):
		super().__init__(
			name='Fists',
			description='Your bare fists.',
			value=0,
			damage=2
		)
	
class Rock(Weapon):
	def __init__(self):
		super().__init__(
			name='Rock',
			description='A fist-sized rock, suitable for bludgeoning.',
			value=1,
			damage=5
		)
			
class Dagger(Weapon):
	def __init__(self):
		super().__init__(
			name='Dagger',
			description='A small dagger with some rust. Somewhat more dangerous than a rock.',
			value=10,
			damage=10
		)
