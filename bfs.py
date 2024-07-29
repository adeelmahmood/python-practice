from collections import deque


def bfs(graph, start):
    visited = set()
    q = deque([start])
    traversed = []

    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            print("processed", node)
            traversed.append(node)
            q.extend([n for n in graph[node] if n not in visited])

    return traversed


graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["B", "H"],
    "F": ["C"],
    "G": ["C"],
    "H": ["E"],
}

start_node = "A"
print(bfs(graph, start_node))
