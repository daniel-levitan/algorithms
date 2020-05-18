def recursive_dfs(graph, start, path=[]):
	path = path + [start]
	for node in graph[start]:
		if not node in path:
			path=recursive_dfs(graph, node, path)
	return path
