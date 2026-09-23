import heapq

def prim(graph, start):
    visited = set()
    heap = [(0, start, None)]
    mst = []
    cost = 0

    while heap:
        weight, vertex, parent = heapq.heappop(heap)

        if vertex in visited:
            continue

        visited.add(vertex)

        if parent is not None:
            mst.append((parent, vertex, weight))
            cost += weight

        for neighbour, w in graph[vertex]:
            if neighbour not in visited:
                heapq.heappush(heap, (w, neighbour, vertex))

    return mst, cost


# USER INPUT
n = int(input("Enter number of vertices: "))

graph = {i: [] for i in range(n)}

e = int(input("Enter number of edges: "))

print("Enter edges as: vertex1 vertex2 weight")

for i in range(e):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))


start = int(input("Enter starting vertex: "))

mst, cost = prim(graph, start)

print("\nPrim's MST:")

for u, v, w in mst:
    print(u, "--", v, "=", w)

print("Total Cost:", cost)