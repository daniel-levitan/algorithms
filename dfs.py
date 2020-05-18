def dfs(graph, start, path=[]):
  queue =[start]
  while queue :
    node = queue .pop(0)
    if node not in path:
      path += [node]
      queue = graph[node] + queue
  return path
