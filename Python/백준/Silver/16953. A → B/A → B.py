a, b = [*map(int, input().split())]

cnt = 1
while a < b:
    if not (b % 2):
        b //= 2
        cnt += 1
    else:
        if b % 10 == 1:
            b //= 10
            cnt += 1
        else:
            cnt = -1
            break
if a > b:
    cnt = -1
print(cnt)