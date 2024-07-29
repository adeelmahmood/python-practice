n = 4
dependencies = [[0, 1], [0, 2], [1, 3], [2, 3]]

from collections import deque


def find_deps(deps, n):
    graph = {}
    in_degree = [0] * n

    # init graph with edges
    for a, b in deps:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        in_degree[b] += 1

    print(graph)
    print(in_degree)

    # start with ones that dont have any dep
    q = deque([i for i in range(n) if in_degree[i] == 0])
    print(q)

    while q:
        node = q.popleft()
        print("task can do", node)

        for n in graph.get(node, []):
            in_degree[n] -= 1
            if in_degree[n] == 0:
                q.append(n)

    pass


find_deps(dependencies, n)
