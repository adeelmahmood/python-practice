from collections import deque, defaultdict


def task_scheduling(n, dependencies):
    # Create an adjacency list
    adj_list = defaultdict(list)
    # Create an array to count the in-degrees of each node
    in_degree = [0] * n

    # Fill the adjacency list and in-degree array
    for a, b in dependencies:
        adj_list[a].append(b)
        in_degree[b] += 1
    print(adj_list)
    print(in_degree)

    # Queue for nodes with no incoming edges
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    print(queue)
    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        # Decrease the in-degree of each neighbor by 1
        for neighbor in adj_list[node]:
            in_degree[neighbor] -= 1
            # If in-degree becomes 0, add the neighbor to the queue
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Check if the topological sort includes all nodes
    if len(topo_order) == n:
        return topo_order
    else:
        # There is a cycle, hence no valid order
        return []


# Example usage
n = 4
dependencies = [[0, 1], [0, 2], [1, 3], [2, 3]]
print(task_scheduling(n, dependencies))  # Expected Output: [0, 1, 2, 3] or [0, 2, 1, 3]
