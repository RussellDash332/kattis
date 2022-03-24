import sys

n = int(input())
arr = []
for line in sys.stdin:
    arr.append(int(line))

def inv_idx(arr, left, right):
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

print(inv_idx(arr, 0, n - 1))