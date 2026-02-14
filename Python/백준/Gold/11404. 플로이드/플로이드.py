n = int(input())
m = int(input())

graph = [[1e11 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    s, e, w = [*map(int, input().split())]
    graph[s-1][e-1] = min(w, graph[s-1][e-1])
    
for k in range(n):
    for x in range(n):
        for y in range(n):
            graph[x][y] = min(graph[x][y], graph[x][k]+graph[k][y])
            
for x in range(n):
    for y in range(n):
        if x == y or graph[x][y] == 1e11:
            print(0, end=" ")
        else:
            print(graph[x][y], end=" ")
    print()
   
