def bfs(graph, start, path=[]):
  queue = [start]
  while queue :
    node = queue.pop(0)
    if not node in path:
      path += [node]
      queue += graph[node]
  return path

print(bfs(graph,'you'))
