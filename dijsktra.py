import heapq

def dijkstra(graph, start):

    distance = {v: float('inf') for v in graph}
    distance[start] = 0

    heap = [(0, start)]

    while heap:

        current_distance, current = heapq.heappop(heap)

        # Skip if already found a shorter path
        if current_distance > distance[current]:
            continue

        for neighbour, weight in graph[current]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
                heapq.heappush(heap, (new_distance, neighbour))

    return distance


# -------- USER INPUT --------

n = int(input("Enter number of vertices: "))

graph = {i: [] for i in range(n)}

e = int(input("Enter number of edges: "))

print("Enter edges as: vertex1 vertex2 weight")

for i in range(e):
    u, v, w = map(int, input().split())

    graph[u].append((v, w))
    graph[v].append((u, w))


start = int(input("Enter starting vertex: "))

# Run Dijkstra
distance = dijkstra(graph, start)

print("\nShortest distances from vertex", start)

for vertex in distance:
    print(start, "->", vertex, "=", distance[vertex])