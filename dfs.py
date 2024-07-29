def dfs(graph, start):
    visited = set()
    traversed = []

    def dfs_recursive(node):
        if node in visited:
            return

        visited.add(node)
        traversed.append(node)
        for n in graph[node]:
            dfs_recursive(n)

    dfs_recursive(start)
    return traversed


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": [],
}

start_node = "A"
print(dfs(graph, start_node))  # Output might be ['A', 'B', 'D', 'E', 'C', 'F', 'G']
