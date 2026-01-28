def solution(triangle):
    answer = 0
    for idx, line in enumerate(triangle):
        if idx == 0:
            continue
        len_ = len(line)
        for i, num in enumerate(line):
            if i == 0:
                triangle[idx][i] += triangle[idx-1][i]
            elif i == len_ - 1:
                triangle[idx][i] += triangle[idx-1][i-1]
            else:
                triangle[idx][i] += max(triangle[idx-1][i-1],triangle[idx-1][i])
    answer = max(triangle[-1])
    return answer