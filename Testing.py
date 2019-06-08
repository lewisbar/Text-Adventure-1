from world import *

w = World()
w._map[7][2].is_explored = True
for y, row in enumerate(w._map):
	for x, room in enumerate(row):
		if w.has_explored_neighbors(x, y):
			print(x, y)

print(w.map_str(x=2, y=5, mode='outline'))
print(w.map_str(x=2, y=5, mode='reveal'))
