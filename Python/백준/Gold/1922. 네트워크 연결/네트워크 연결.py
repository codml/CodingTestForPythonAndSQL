import sys; input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)
    
    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            rank[y] += 1

def kruskal(v, edges):
    mst_weights = 0
    mst_edges = 0
    parent = [i for i in range(v+1)]
    rank = [0 for _ in range(v+1)]
    
    edges.sort()
    for w, x, y in edges:
        if find(parent, x) != find(parent, y):
            union(parent, rank, x, y)
            mst_weights += w
            mst_edges += 1
            
            if mst_edges >= v - 1:
                break
    return mst_weights

v = int(input())
e = int(input())
edges = []
for _ in range(e):
    x, y, w = [*map(int, input().split())]
    edges.append((w, x, y))
print(kruskal(v, edges))