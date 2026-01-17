from collections import deque

def bfs(maps):
    q = deque()
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q.append((0,0))
    while q:
        x,y = q.popleft()
        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return maps[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                q.append((nx,ny))
                maps[nx][ny] += maps[x][y]
    return -1

def solution(maps):
    return bfs(maps)