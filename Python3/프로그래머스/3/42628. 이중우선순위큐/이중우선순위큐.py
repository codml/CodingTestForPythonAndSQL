from heapq import heappush, heappop

def solution(operations):
    min_heap = []
    max_heap = []
    visited = [False] * len(operations)
    answer = []
    
    for i, cmd in enumerate(operations):
        c, num = cmd.split()
        if c == 'I':
            heappush(min_heap, (int(num), i))
            heappush(max_heap, (-1*int(num), i))
        else:
            if num == '1':
                while max_heap and visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    _, i = heappop(max_heap)
                    visited[i] = True
            else:
                while min_heap and visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    _, i = heappop(min_heap)
                    visited[i] = True
    while min_heap and visited[min_heap[0][1]]:
        heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]:
        heappop(max_heap)
    if min_heap:
        answer.append(-1 * max_heap[0][0])
        answer.append(min_heap[0][0])
    else:
        answer.extend([0,0])
    return answer