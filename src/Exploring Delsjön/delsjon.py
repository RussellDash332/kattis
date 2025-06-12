def extend(t, k):
    p = t
    for _ in range(k):
        for i in range(len(A)): A[i].append(A[i][p]+1)
        A.append([A[i][-1] for i in range(len(A))]); A[-1].append(0); p = len(A)-1
N = int(input())
D = [[*map(int, input().split())] for _ in range(N)]
A = [[0]]; M = [0]
for i in range(1, N):
    for j in range(len(A)):
        u = D[i][0]-A[j][M[0]]
        for k in range(1, i):
            if u != D[i][k]-A[j][M[k]]: u = -1; break
        if u > 0: break
    extend(j, u); M.append(len(A)-1)
S = {e:i for i,e in enumerate(M+sorted({*range(len(A))}-{*M}))}
print(len(A))
for i in range(len(A)):
    for j in range(i):
        if A[i][j] == 1: print(S[i]+1, S[j]+1)