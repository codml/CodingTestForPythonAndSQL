import sys; input = sys.stdin.readline
from collections import deque

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    x = find(parent, x)
    y = find(parent, y)
    
    if x == y:
        return
    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[y] = x
        rank[x] += 1

def is_union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    
    if x == y:
        return 'YES'
    return 'NO'
        
q = deque()
n, m = [*map(int, input().split())]

parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]
for _ in range(m):
    s, a, b = [*map(int, input().split())]
    if s: # FIND
        q.append(is_union(parent, a, b))
    else:
        union(parent, rank, a, b)
while q:
    print(q.popleft())
        
        
        
    