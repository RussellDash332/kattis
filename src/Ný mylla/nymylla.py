N, M, K = map(int, input().split())
G = [[0]*101 for _ in range(101)]
for n in range(1, 101):
    for m in range(1, n+1):
        if n+m-1 < K: continue
        S = 0
        for i in range(-~n//2):
            L = [a^b for a, b in zip(G[i], G[n-1-i])]
            for j in range(-~m//2): S |= 1<<(L[j]^L[m-1-j])
        G[n][m] = G[m][n] = ((S+1)&~S).bit_length()-1
print('SFeyirnrnii!!'[G[N][M]>0::2])