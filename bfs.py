graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

from collections import deque


def bfsLookFor(name):
	search_queue = deque()
	search_queue += graph['you']
	searched = []

	while search_queue:
		person = search_queue.popleft()
		if not person in searched:
			if person == name:
				print('Encontrei', name)
				return True
			else: 
				search_queue += graph[person]
				searched.append(person)
	return False

print(bfsLookFor('thom'))