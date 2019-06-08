class Action():
	def __init__(self, name, hotkey, method):
		self.name = name
		self.hotkey = hotkey
		self.method = method
	
	def __str__(self):
		return self.hotkey + ': ' + self.name
