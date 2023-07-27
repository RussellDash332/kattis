N, t = map(int, input().split())

mem = {}
def f(N, d):
    if d == 0: return N == 0
    if t*((1<<d)-1) < N: return 0
    if (N, d) in mem: return mem[(N, d)]
    s = 0
    for i in range(t+1):
        if (i<<(d-1)) <= N: s += f(N-(i<<(d-1)), d-1)
    s %= 998244353; mem[(N, d)] = s; return s

print(f(N, len(bin(N))-2))