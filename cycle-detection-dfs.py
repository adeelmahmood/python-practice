# Question:
# Implement a function to detect if a directed graph has a cycle.
# Use DFS to determine if there is any node that is part of a cycle.


graph_with_cycle = {"A": ["B"], "B": ["C"], "C": ["A"], "D": ["E"], "E": ["F"], "F": []}
# Expected Output: True (Cycle exists: A -> B -> C -> A)
graph_without_cycle = {"A": ["B"], "B": ["C"], "C": [], "D": ["E"], "E": ["F"], "F": []}
# Expected Output: False (No cycle)
graph_with_multiple_cycles = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": ["A"],  # Cycle: A -> B -> D -> A
    "E": ["C"],  # Cycle: C -> E -> C
}
# Expected Output: True (Multiple cycles exist)
disconnected_graph_without_cycle = {
    "A": ["B"],
    "B": [],
    "C": ["D"],
    "D": [],
    "E": ["F"],
    "F": [],
}
# Expected Output: False (No cycle)


def dfs(graph):
    visited = set()
    stack = set()

    def dfs_recurise(node):
        if node in stack:
            return True  # cycle
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        # explore neighbords
        for n in graph[node]:
            if dfs_recurise(n):
                return True

        stack.remove(node)

    for node in graph:
        if node not in visited:
            if dfs_recurise(node):
                return True

    return False


print(dfs(graph_with_cycle))
print(dfs(graph_with_multiple_cycles))
print(dfs(graph_without_cycle))
print(dfs(disconnected_graph_without_cycle))
