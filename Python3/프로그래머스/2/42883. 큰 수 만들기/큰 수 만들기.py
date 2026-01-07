def solution(number, k):
    answer = []
    cnt = 0
    
    for idx, n in enumerate(number):
        if cnt == k:
            for i in range(idx, len(number)):
                answer.append(number[i])
            break
        while answer and answer[-1] < n and cnt < k:
            answer.pop()
            cnt += 1
        if len(answer) < len(number) - k:
            answer.append(n)
        
    return ''.join(answer)
	