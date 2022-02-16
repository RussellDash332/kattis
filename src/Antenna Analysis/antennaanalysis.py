n, c = list(map(int, input().split()))
arr = list(map(int, input().split()))
term = [-float("inf")] * n

m = arr[0] - c
for i in range(n):
    t = arr[i] - c * (i + 1)
    m = min(m, t)
    term[i] = max(term[i], t - m)

m = -arr[0] - c
for i in range(n):
    t = -arr[i] - c * (i + 1)
    m = min(m, t)
    term[i] = max(term[i], t - m)

print(*term)