def kitamasa(c, a, n):
    k = len(c)
    def m(x, y):
        z = [0]*(2*k+1)
        for i in range(k+1):
            if x[i]:
                for j in range(k+1): z[i+j] = (z[i+j]+x[i]*y[j])%M
        for i in range(2*k, k, -1):
            if z[i]:
                for j in range(k): z[i-j-1] = (z[i-j-1]+z[i]*c[j])%M
        return z[:k+1]
    b = [0, 1]+[0]*~-k; v = [1]+[0]*k; n += 1
    while n:
        if n%2: v = m(v, b)
        b = m(b, b); n >>= 1
    return sum(x*y for x,y in zip(a,v[1:]))%M
M = 10**9+7; N, K = map(int, input().split()); K -= 1
print(kitamasa([1]*K, [0]*~-K+[1], N+K-2))