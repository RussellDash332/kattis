n = int(input()); S = []; P = []; E = []; A = []
for _ in range(n): s, p, e, a = map(int, input().split()); S.append(s); P.append(p); E.append(e); A.append(a)
D = [[-10**18]*(_+2) for _ in range(n+1)]; D[0][0] = 0; E.append(0)
for i in range(n):
    for j in range(i+2):
        D[i+1][j] = max(D[i+1][j], D[i][j]+S[i]-E[i-1]) # fail
        if D[i][j-1]+S[i]-E[i-1] >= A[i]: D[i+1][j] = max(D[i+1][j], D[i][j-1]+S[i]-E[i-1]-A[i]+E[i]-P[i]) # pass
print(max((i for i in range(n+1) if D[n][i] >= 0), default=0))