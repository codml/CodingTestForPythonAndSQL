n = int(input())
li = [*map(int,input().split())]

m = 1+2e8

l = 0
r = n-1
while l < r:
    s = li[l] + li[r]
    m = s if abs(s) < abs(m) else m
    
    if s == 0:
        break
    elif s > 0:
        r -= 1
    else:
        l += 1
print(m)