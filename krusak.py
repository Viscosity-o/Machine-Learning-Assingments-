def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if root_x != root_y:

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y

        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        else:
            parent[root_y] = root_x
            rank[root_x] += 1


def kruskal(vertices, edges):

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    mst = []
    cost = 0

    for u, v, w in edges:

        if find(parent, u) != find(parent, v):

            union(parent, rank, u, v)

            mst.append((u, v, w))
            cost += w

    return mst, cost


# USER INPUT
n = int(input("Enter number of vertices: "))

vertices = list(range(n))

e = int(input("Enter number of edges: "))

edges = []

print("Enter edges as: vertex1 vertex2 weight")

for i in range(e):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))


mst, cost = kruskal(vertices, edges)

print("\nKruskal's MST:")

for u, v, w in mst:
    print(u, "--", v, "=", w)

print("Total Cost:", cost)