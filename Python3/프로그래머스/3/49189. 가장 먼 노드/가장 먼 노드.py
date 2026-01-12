from collections import deque

def solution(n, edge):
    answer = 0
    
    graph = {}
    for i in range(n+1):
        graph[i] = []
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    visited = [0] * (n+1)
    queue = deque()
    
    queue.append(1)
    visited[1] = 1
    while queue:
        cur = queue.popleft()
        for next_ in graph[cur]:
            if not visited[next_]:
                visited[next_] = visited[cur] + 1
                queue.append(next_)
    
    max_ = max(visited)
    for node in visited:
        if max_ == node:
            answer += 1
    return answer