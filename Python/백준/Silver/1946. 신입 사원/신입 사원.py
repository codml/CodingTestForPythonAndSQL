import sys; input = sys.stdin.readline

T = int(input())
answer = []
for _ in range(T):
    N = int(input())
    people = []
    for _ in range(N):
        # d: 1차 서류, i: 2차 면접
        d, i = [*map(int, input().split())]
        people.append((d,i))
    # d를 기준으로 정렬
    people.sort()
    i_min = N
    cnt = N
    for person in people:
        if person[1] > i_min:
            cnt -= 1
        else:
            i_min = person[1]
    answer.append(cnt)
for ans in answer:
    print(ans)