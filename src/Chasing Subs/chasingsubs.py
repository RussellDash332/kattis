s = input(); t = input(); P = 31; M = 10**9+7; Hs = [[0]*(len(s)+1) for _ in range(26)]; Ht = [[0]*(len(t)+1) for _ in range(26)]; Q = [1]; I = [1]; V = pow(P, -1, M)
for i in range(250000): Q.append(Q[-1]*P%M); I.append(I[-1]*V%M)
for i in range(26):
    for j in range(len(s)): Hs[i][j+1] = (Hs[i][j]+Q[j]*(ord(s[j])-97==i))%M
    for j in range(len(t)): Ht[i][j+1] = (Ht[i][j]+Q[j]*(ord(t[j])-97==i))%M
print(s[Z[0]:Z[0]+len(t)] if len(Z:=[i for i in range(len(s)-len(t)+1) if sorted(Ht[j][-1] for j in range(26))==sorted((Hs[j][i+len(t)]-Hs[j][i])*I[i]%M for j in range(26))]) == 1 else len(Z))