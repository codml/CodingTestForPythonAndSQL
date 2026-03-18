import sys; input = sys.stdin.readline

## 데이터 입력
n, m = map(int, input().split())
brd = []
for row in range(n):
    brd.append(input()) # 문자열도 배열처럼 조회 가능

min_chg = 64 # 최소 변경 횟수를 저장할 변수
## 전체 판을 순회
for row in range(n - 8 + 1):
    for col in range(m - 8 + 1):
        b_chg = 0 # B가 좌상단일 때 다시 칠해야 할 칸
        w_chg = 0 # W가 좌상단일 때 다시 칠해야 할 칸
        for i in range(8):
            for j in range(8):
                if not (i+j) % 2:
                    if brd[row+i][col+j] != 'B':
                        b_chg += 1
                    else:
                        w_chg += 1
                else:
                    if brd[row+i][col+j] != 'W':
                        b_chg += 1
                    else:
                        w_chg += 1
        min_chg = min(min_chg, min(b_chg, w_chg)) # 기존 최소 횟수와 비교
print(min_chg)