import sys; input = sys.stdin.readline
from collections import deque

T = int(input())
ans = deque()
for _ in range(T):
    N, K = [*map(int, input().split())]
    D = [0, *map(int, input().split())]
 
    graph = [[] for _ in range(N+1)]
    degree = [0 for _ in range(N+1)]
    build = [0 for _ in range(N+1)]
    for _ in range(K):
        X, Y = [*map(int, input().split())]
        graph[X].append(Y)
        degree[Y] += 1
    W = int(input())

    q = deque()
    for i in range(1, N+1):
        if not degree[i]:
            q.append(i)
            build[i] = D[i]

    while q:
        node = q.popleft()
    
        for next_ in graph[node]:
            degree[next_] -= 1
            build[next_] = max(build[next_], D[next_] + build[node])
            if not degree[next_]:
                q.append(next_)
                
    ans.append(build[W])
while ans:
    print(ans.popleft())