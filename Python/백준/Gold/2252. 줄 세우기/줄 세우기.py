import sys; input = sys.stdin.readline
from collections import deque

n, m = [*map(int, input().split())]
graph = [[] for _ in range(n+1)]
in_degree = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = [*map(int, input().split())]
    graph[a].append(b)
    in_degree[b] += 1

q = deque()
for i in range(1, n+1):
    if not in_degree[i]:
        q.append(i)

result = []
while q:
    node = q.popleft()
    result.append(node)
    
    for next_node in graph[node]:
        in_degree[next_node] -= 1
        if not in_degree[next_node]:
            q.append(next_node)
            
for node in result:
    print(node, end=" ")