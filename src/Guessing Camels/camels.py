n = int(input())
x, y, z = [list(map(int, input().split())) for _ in range(3)]

def inv_idx(arr, left=0, right=n-1):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += inv_idx(arr, left, mid) + inv_idx(arr, mid + 1, right)
        inv_count += merge(arr, left, mid, right)
    return inv_count

def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    inv_count = 0
    temp = []
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            inv_count += (mid - i + 1)
            j += 1
    temp.extend(arr[i:mid+1])
    temp.extend(arr[j:right+1])
    for idx in range(left, right + 1):
        arr[idx] = temp[idx - left]
    return inv_count

p = 0
for a, b in ((x, y), (y, z), (z, x)):
    a2 = {e: i for i, e in enumerate(a)}
    p += inv_idx([a2[e] for e in b])
print(n*(n-1)//2 - p//2)