import sys; input = sys.stdin.readline

n, m = map(int, input().split())

brd = []
for row in range(n):
    brd.append([*input().split()[0]])

cnt = 64
for row in range(n - 8 + 1):
    for col in range(m - 8 + 1):
        bcnt = 0
        wcnt = 0
        for i in range(8):
            for j in range(8):
                if not (i+j) % 2:
                    if brd[row+i][col+j] != 'B':
                        bcnt += 1
                    else:
                        wcnt += 1
                else:
                    if brd[row+i][col+j] != 'W':
                        bcnt += 1
                    else:
                        wcnt += 1
        cnt = min(cnt, min(bcnt, wcnt))
print(cnt)