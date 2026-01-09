def length(trees, idx):
    leng = 0
    for tree in trees:
        leng += tree - idx if tree > idx else 0
    return leng

def binary_search(trees, value, f, r):
    if f > r:
        return r
    mid = (f + r) // 2
    if length(trees, mid) == value:
        return mid
    elif length(trees, mid) < value:
        return binary_search(trees, value, f, mid-1)
    else:
        return binary_search(trees, value, mid+1, r)

_, m = map(int, input().split())
trees = [*map(int, input().split())]

max_ = max(trees)
answer = binary_search(trees, m, 0, max_)
print(answer)