from bisect import bisect_left

input()
arr = [*map(int, input().split())]
lis = []

for num in arr:
    if not lis:
        lis.append(num)
    elif lis[-1] < num:
        lis.append(num)
    else:
        lis[bisect_left(lis, num)] = num
print(len(lis))