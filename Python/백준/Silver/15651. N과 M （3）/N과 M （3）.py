n, m = [*map(int, input().split())]

path = []

def backtrack():
    if len(path) == m:
        for num in path:
            print(num, end=" ")
        print()
        return
    
    for i in range(1, n+1):
        path.append(i)
        backtrack()
        path.pop()
        
backtrack()