def cal_lan(arr, n, mid):
    cnt = 0
    for num in arr:
        cnt += num // mid
    return cnt >= n

def upper_bound(arr, n, l, r):
    while l < r:
        mid = l + (r - l) // 2
        
        if cal_lan(arr, n, mid):
            l = mid + 1
        else:
            r = mid
    return l - 1

k, n = [*map(int, input().split())]
arr = []
for _ in range(k):
    arr.append(int(input()))
print(upper_bound(arr, n, 0, max(arr)+1))