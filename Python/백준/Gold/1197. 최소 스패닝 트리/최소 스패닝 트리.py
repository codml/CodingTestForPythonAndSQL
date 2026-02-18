import sys; input = sys.stdin.readline

# Union-Find (최적화 X)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a != b:
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[a] = b
            rank[b] += 1

# Kruskal Algorithm
def kruskal(v, edges):
    mst_weight = 0
    mst_edges = 0
    parent = [i for i in range(v + 1)] # MakeSet
    rank = [0 for _ in range(v + 1)]

    edges.sort() # edges가 (weight, node_1, node_2로 구성되어 있다고 가정)

    for weight, a, b in edges:
        if find(parent, a) != find(parent, b): # 서로 다른 집합 -> 사이클 X
            union(parent, rank, a, b) # 간선을 추가하면 이제 같은 집합
            mst_weight += weight
            mst_edges += 1

            if mst_edges == v - 1: # 모든 간선을 보기 전에 이미 MST가 완성
                break
    if mst_edges < v - 1:
        mst_weight = -1 # MST를 만들 수 없음
    return mst_weight

v, e = [*map(int, input().split())]
edges = []
for _ in range(e):
    a, b, w = [*map(int, input().split())]
    edges.append((w, a, b))
print(kruskal(v, edges))