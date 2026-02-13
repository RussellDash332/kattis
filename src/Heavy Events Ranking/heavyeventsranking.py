n = int(input()); E = {}; S = {}; Z = {}; F = {}; T = {}; H = {}
for _ in range(8*n): a, e, s = input().split(); S[a] = S.get(a, 0); F[a] = F.get(a, 0); T[a] = T.get(a, 0); H[a] = H.get(a, 0); E[e] = E.get(e, [])+[(eval(s), a)]
for e in E:
    E[e].sort(reverse=1); i = 0
    while i < n:
        k = 1
        while i+k < n and E[e][i][0] == E[e][i+k][0]: k += 1
        for j in range(i, i+k):
            S[E[e][j][1]] += i+(k+1)/2
            if i < 2: (F, T, H)[i][E[e][j][1]] -= 1
        i += k
for a in S: Z[k] = Z.get(k:=(S[a], F[a], T[a], H[a]), [])+[a]
m = min(Z)
if len(Z[m]) > 1: print('tie', m[0])
else: print(Z[m][0], m[0])