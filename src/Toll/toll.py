import sys; input = sys.stdin.readline
K, N, M, O = map(int, input().split()); B = 0; V = 1
while V < N: V *= 2; B += 1
J = [10**9]*B*K*N
for _ in range(M): a, b, w = map(int, input().split()); J[a*B*K+B*(b%K)] = w
for i in range(1, B):
    for a in range(N):
        for b in range(K):
            v = (a//K+(1<<(i-1)))*K+b
            if v < N: 
                for c in range(K): J[a*B*K+B*c+i] = min(J[a*B*K+B*c+i], J[a*B*K+B*b+i-1]+J[v*B*K+B*c+i-1])
for _ in range(O):
    a, b = map(int, input().split()); d = b//K-a//K; z = [10**9]*K; z[a%K] = 0; ga = a//K
    for i in range(B-1, -1, -1):
        if d&(1<<i): z = [min(z[k]+J[(ga*K+k)*B*K+B*j+i] for k in range(K) if ga*K+k < N) for j in range(K)]; ga += 1<<i
    r = z[b%K]; print(r if r < 10**9 else -1)