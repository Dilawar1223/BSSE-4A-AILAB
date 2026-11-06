from collections import deque
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}
queue = deque([('A', ['A'])])
visited = []
while queue:
    node, path = queue.popleft()
    visited.append(node)

    if node == 'G':
        break

    for n in graph[node]:
        queue.append((n, path + [n]))
print("BFS Path:", path)
print("BFS Visit Order:", visited)
stack = [('A', ['A'])]
visited = []
while stack:
    node, path = stack.pop()
    visited.append(node)
    if node == 'G':
        break
    for n in reversed(graph[node]):
        stack.append((n, path + [n]))
print("DFS Path:", path)
print("DFS Visit Order:", visited)
