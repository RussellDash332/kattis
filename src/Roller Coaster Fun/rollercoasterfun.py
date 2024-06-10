import sys; input = sys.stdin.readline
N = int(input()); M = 25001; D = [0]*M
for _ in range(N):
    a, b, t = map(int, input().split())
    if b:
        k = 1; F = 0; E = [*D]
        while (f:=a-(k-1)**2*b) > 0:
            F += f
            for tt in range(M-k*t): E[tt+k*t] = max(E[tt+k*t], D[tt]+F)
            k += 1
        D = E
    else:
        for tt in range(M-t): D[tt+t] = max(D[tt+t], D[tt]+a)
for _ in range(int(input())): print(D[int(input())])