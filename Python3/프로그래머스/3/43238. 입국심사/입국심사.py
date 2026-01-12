def cal_people(arr, time, target):
    people = 0
    flag = False
    for a in arr:
        people += time // a
        if people > target:
            break
        if not flag and time % a == 0:
            flag = True
    return people, flag

def binary_search(arr, target, f, r):
    if f > r:
        return f
    mid = (f + r) // 2
    people, flag = cal_people(arr, mid, target)
    if people == target and flag:
        return mid
    elif (people == target and not flag) or people > target:
        return binary_search(arr, target, f, mid-1)
    else:
        return binary_search(arr, target, mid+1, r)
    
def solution(n, times):
    min_ = min(times)
    answer = binary_search(times, n, 0, min_*n)
    return answer