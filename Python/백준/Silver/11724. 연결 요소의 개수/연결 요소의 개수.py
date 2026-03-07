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
            parent[y] = x
            rank[x] += 1

def solution(v, edges):
    parent = [i for i in range(v+1)]
    rank = [0 for _ in range(v+1)]
    cnt = 0
    
    for x, y in edges:
        if find(parent, x) != find(parent, y):
            union(parent, rank, x, y)
    
    for i in range(1, v+1):
        if i == parent[i]:
            cnt += 1
    return cnt

v, n = [*map(int, input().split())]
edges = []
for _ in range(n):
    x, y = [*map(int, input().split())]
    edges.append((x,y))

print(solution(v, edges))