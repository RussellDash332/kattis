import sys; input = sys.stdin.readline
for _ in range(int(input())):
    T, N = map(int, input().split())
    c = [1]*(T+1)
    for _ in range(N):
        d = [0]*(T+1); t1, t2 = map(int, input().split()); v = t2-t1
        for i in range(T+1):
            if c[i] and i>=v: d[i-v] = 1
            if c[i] and i<=T-v: d[i+v] = 1
        c = d
    if sum(d) == 0: print('impossible'), exit(0)
print('possible')