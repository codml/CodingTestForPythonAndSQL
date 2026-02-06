import sys
input = sys.stdin.readline
from heapq import heappush, heappop

v, e = [*map(int, input().split())]
s = int(input())

heap = []
dist = [1e8 for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
visited = [False for _ in range(v+1)]

for _ in range(e):
    a, b, w = [*map(int, input().split())]
    graph[a].append((w, b))

dist[s] = 0
heappush(heap, (0, s))
while heap:
    cur = heappop(heap)
    if visited[cur[1]]:
        continue
    visited[cur[1]] = True
    
    for weight, vertex in graph[cur[1]]:
        if dist[vertex] > cur[0] + weight:
            dist[vertex] = cur[0] + weight
            heappush(heap, (dist[vertex], vertex))
            
for i in range(1, v+1):
    if dist[i] == 1e8:
        print('INF')
    else:
        print(dist[i])