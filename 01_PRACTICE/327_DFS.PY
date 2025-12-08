from collections import defaultdict

graph = defaultdict(list)
graph[0] = [1, 2]
graph[1] = [3]
graph[2] = [4]

def dfs(node, visited=set()):
    print(node, end=" ")
    visited.add(node)
    for nei in graph[node]:
        if nei not in visited:
            dfs(nei, visited)

dfs(0)
