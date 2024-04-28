import sys; input = sys.stdin.readline
n = int(input()); a = [*map(int, input().split())]; idx = 0
for i in range(63, -1, -1):
    mi = idx; mv = 0
    for j in range(idx, n):
        if a[j]&(1<<i) != 0 and a[j] > mv: mv = a[j]; mi = j
    if mv == 0: continue
    a[idx], a[mi] = a[mi], a[idx]; mi = idx
    for j in range(n):
        if j != mi and a[j]&(1<<i) != 0: a[j] ^= a[mi]
    idx += 1
res = 0
for i in range(n): res = res ^ a[i]
print(res)