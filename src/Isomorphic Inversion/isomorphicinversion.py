s = [*map(int, input())]; n = len(s)
p = 31; M = 10**9+7
e = [pow(p, i, M) for i in range(n)]
P = S = a = v = 0
for i in range(n):
    P += e[v]*s[i]; P %= M; v += 1
    S *= p; S += s[n-1-i]; S %= M
    if P == S: a += 1; P = S = v = 0
print(a)