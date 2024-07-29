# Question:
# You are given a list of tasks with their dependencies.
# Each task is represented by a string, and dependencies are represented as
# a pair (task, dependency). Implement a function to find a valid order to
# complete all tasks, considering their dependencies.

tasks_1 = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
# Expected Output: ['D', 'B', 'C', 'A'] or any valid topological order
tasks_2 = {"A": ["B"], "B": ["C"], "D": ["C"], "C": []}
# Expected Output: ['C', 'B', 'A', 'D'] or ['C', 'B', 'D', 'A'] or any valid topological order
tasks_3 = {"X": ["Y"], "Y": ["Z"], "Z": []}
# Expected Output: ['Z', 'Y', 'X']
tasks_4 = {"A": [], "B": [], "C": [], "D": []}
# Expected Output: ['A', 'B', 'C', 'D'] or any permutation of ['A', 'B', 'C', 'D']
# tasks_5 = {"A": ["B"], "B": ["C"], "C": ["A"]}
# Expected Output: No valid topological order (cycle detected)

courses = {"Math": ["Physics"], "Physics": ["Chemistry"], "Chemistry": []}


from collections import deque


def tsort(graph):
    sorted = []
    # create indegree graph
    in_degrees = {node: 0 for node in graph}
    # calculate in degrees
    for node in graph:
        for n in graph[node]:
            in_degrees[n] += 1

    queue = deque([node for node in graph if in_degrees[node] == 0])

    while queue:
        node = queue.popleft()

        sorted.append(node)

        # since this node has been processed, reduce deps
        for n in graph[node]:
            in_degrees[n] -= 1
            if in_degrees[n] == 0:
                queue.append(n)

    if len(sorted) != len(graph):
        raise ValueError("Graph contains a cycle")

    return sorted[::-1]


print(tsort(tasks_1))
print(tsort(tasks_2))
print(tsort(tasks_3))
print(tsort(tasks_4))
print(tsort(courses))
