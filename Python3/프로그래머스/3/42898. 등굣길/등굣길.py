def solution(m, n, puddles):
    road = [0 for _ in range(m+1)]
    
    for y in range(1, n+1):
        for x in range(1, m+1):
            if [x,y] in puddles:
                road[x] = 0
                continue
            prev = road[x-1]
            if (x == 1 and y == 1):
                prev = 1
            road[x] = ((road[x]%1000000007)+(prev%1000000007))%1000000007

    return road[m] % 1000000007