# Question:
# Given a graph, write a function that returns all nodes that are exactly k steps away
# from a given starting node. Use BFS to explore the graph.

graph = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "E"], "D": ["B"], "E": ["C"]}
start_node = "A"
k = 2


from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([(start, start, 0)])  # (orignode, node, dist)
    result = []

    while queue:
        orig, node, dist = queue.popleft()

        if node not in visited:
            print(orig, node, dist)

            if dist == k and node != start:
                # print("adding ", node, dist, k)
                result.append(node)

            visited.add(node)

            queue.extend([(node, n, dist + 1) for n in graph[node]])

    print(result)


bfs(graph, start_node)
