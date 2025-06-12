def booth(s):
    n = len(s); f = [-1]*2*n; k = 0
    for j in range(1, 2*n):
        i = f[j-k-1]
        while i != -1 and s[j % n] != s[(k+i+1)%n]:
            if s[j%n] < s[(k+i+1)%n]: k = j-i-1
            i = f[i]
        if i == -1 and s[j%n] != s[(k+i+1)%n]:
            if s[j%n] < s[(k+i+1)%n]: k = j
            f[j-k] = -1
        else: f[j-k] = i+1
    return s[k:]+s[:k]
N, K = map(int, input().split()); A = (1<<N)-1
S = [*map(int, input().replace('W', '1').replace('B', '0'))]
for _ in range(K):
    c = []
    for i in range(N): c.append(S[i]^S[(i+1)%N])
    S = c
T = [int(''.join(map(str, S)), 2)]
for _ in range(K):
    U = set()
    for t in T:
        c = 0
        for i in range(N-1): c = 2*c+((c&1)^(t>>(~i+N)&1))
        if t&1 == (c&1)^(c>>(N-1)): U.add(c); U.add(c^A)
    T = U
print(len({booth(bin(i)[2:].zfill(N)) for i in T}))