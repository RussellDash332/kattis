a = [0]*2001; b = [0]*2001; m = 0; v = [int(input()) for _ in range(int(input()))]; n = len(v)
for i in range(n-1, -1, -1):
    for j in range(i+1, n+1):
        if j == n or v[j] > v[i]: a[i] = max(a[i], a[j]+1)
        if j == n or v[j] < v[i]: b[i] = max(b[i], b[j]+1)
# not really LIS since the base of the LIS is fixed?
print(max([a[i]+b[i]-1 for i in range(n)], default=0))