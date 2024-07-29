# Question:
# Given a directed graph, write a function to find all paths from a start node to an end node.
# Use DFS to explore all possible paths.

graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
start_node = "A"
end_node = "D"

# Expected Output: [['A', 'B', 'D'], ['A', 'C', 'D']]


def all_paths(graph, start, end):
    visited = set()
    paths = []

    def dfs(node, path):
        if node in visited:
            return

        path.append(node)

        if node == end:
            paths.append(list(path))

        for n in graph[node]:
            if n not in visited:
                dfs(n, path)

        path.pop()

    dfs(start, [])
    print(paths)


all_paths(graph, "A", "D")
