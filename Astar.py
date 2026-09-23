
import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):

    rows = len(grid)
    cols = len(grid[0])

    # Priority queue: (f, g, position, path)
    heap = [(0, 0, start, [start])]

    visited = set()

    while heap:

        f, g, current, path = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == goal:
            return path, g

        row, col = current

        # Up, Down, Left, Right
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        for dr, dc in directions:

            nr = row + dr
            nc = col + dc

            if 0 <= nr < rows and 0 <= nc < cols:

                # 0 = free, 1 = obstacle
                if grid[nr][nc] == 1:
                    continue

                neighbour = (nr, nc)

                if neighbour in visited:
                    continue

                new_g = g + 1
                h = heuristic(neighbour, goal)
                f = new_g + h

                heapq.heappush(
                    heap,
                    (f, new_g, neighbour, path + [neighbour])
                )

    return None, None


# ---------------- USER INPUT ----------------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter grid (0 = free path, 1 = obstacle):")

grid = []

for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

start = tuple(map(int, input("Enter start row col: ").split()))
goal = tuple(map(int, input("Enter goal row col: ").split()))


# Run A*
path, cost = astar(grid, start, goal)


# Output
if path:
    print("\nPath found:")
    print(path)

    print("Cost:", cost)

else:
    print("\nNo path found.")