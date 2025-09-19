from queue import Queue
from sys import argv


desired_number = -1
if len(argv) > 1:
	desired_number = int(argv[1])

# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers
# Putting comments here so that you can't see the anvil spoilers

moves = {
    'light_hit': -3,
    'medium_hit': -6,
    'heavy_hit': -9,
    'draw': -15,
    'punch': 2,
    'bend': 7,
    'upset': 13,
    'shrink': 17
}

cache = {}

anvil_size = 150

q = Queue()
q.put(0)
cache[0] = tuple()
while not q.empty():
    curr_point = q.get()
    for move, value in moves.items():
        f_value = curr_point + value
        if f_value >= anvil_size or f_value < 0:
            continue
        if f_value in cache:
            continue
        cache[f_value] = cache[curr_point] + (move,)
        q.put(f_value)

for k, v in cache.items():
	cache[k] = v[::-1]




if desired_number == -1:
	for i in range(anvil_size):
		print(i, cache[i])
else:
	print(cache[desired_number])
