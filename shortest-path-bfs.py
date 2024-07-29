# Question:
# Given an m x n grid with some obstacles (marked as 1) and empty cells (marked as 0),
# find the shortest path from the top-left corner to the bottom-right corner.
# You can only move up, down, left, or right. Return the length of the shortest
# path, or -1 if no path exists.


from collections import deque

grid = [[0, 1, 0, 0], [0, 1, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]]


def shortest_path(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]  # R, U, D, L

    queue = deque([(0, 0, 0)])  # i, j, dist
    visited = set((0, 0))  # i, j

    while queue:
        i, j, dist = queue.popleft()

        # boundary conditions
        if (i, j) == (rows - 1, cols - 1):
            return dist

        # explore neighbors
        for _i, _j in directions:
            ni, nj = i + _i, j + _j
            if (
                ni >= 0
                and ni < rows
                and nj >= 0
                and nj < cols
                and grid[ni][nj] == 0
                and (ni, nj) not in visited
            ):
                queue.append((ni, nj, dist + 1))
                visited.add((ni, nj))

    return -1


print(shortest_path(grid))
