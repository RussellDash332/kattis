n, m, *a = map(int, open(0).read().split()); z = 2*n*(m-1); N = 1<<n
for i in range(m-1):
    v1 = a[i]+N; c1 = 0
    while v1%2==0: v1 //= 2; c1 += 1
    v2 = a[i+1]+N; c2 = 0
    while v2%2==0: v2 //= 2; c2 += 1
    s = 0; v1, v2 = a[i]+N, a[i+1]+N; d = abs(c1-c2)
    if c1 > c2: v2 = (a[i+1]<<d)%N+N
    else: v1 = (a[i]<<d)%N+N
    while v1%2==v2%2 and v1 > 1: s += 1; v1 //= 2; v2 //= 2
    z += d-2*s
print(z)