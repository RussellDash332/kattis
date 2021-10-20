n, m = list(map(int, input().split()))
t = sorted(list(map(int, input().split())))
l = sorted(list(map(int, input().split())))

ans = 0
i, j = 0, 0
while i < n and j < m:
    if t[i] <= l[j]:
        ans += 1
        i += 1
    j += 1

print(ans)