from collections import deque


def topological_sort(graph):
    # in degrees
    in_degrees = {node: 0 for node in graph}
    for node in graph:
        for n in graph[node]:
            in_degrees[n] += 1
    print(in_degrees)

    sorted_arr = []
    q = deque([n for n in graph if in_degrees[n] == 0])
    print(q)

    while q:
        node = q.popleft()
        sorted_arr.append(node)

        for n in graph[node]:
            in_degrees[n] -= 1
            if in_degrees[n] == 0:
                q.append(n)

    if len(sorted) != len(graph):
        raise ValueError("Graph contains a cycle")

    return sorted_arr


# Example usage
graph = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": [],
}

print(
    topological_sort(graph)
)  # Output might be ['A', 'B', 'C', 'D', 'E', 'H', 'F', 'G']
