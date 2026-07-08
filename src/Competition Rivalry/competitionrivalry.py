N = int(input())
E = [[] for _ in range(N)]
R = [[] for _ in range(N)]
X = int(input())
for _ in range(X): p, s, t = map(int, input().split()); p -= 1; E[p].append([s, -t])
Y = int(input())
for _ in range(Y): p, s, t = map(int, input().split()); p -= 1; R[p].append([s, -t])
for i in range(N):
    for A in (E, R):
        A[i].sort(key=lambda x:-x[1])
        for j in range(len(A[i])): A[i][j].append(-j)
M_e = [max(x) for x in E if x]
M_r = [max(x) for x in R if x]
S_e = sum(k[0] for k in M_e)
S_r = sum(k[0] for k in M_r)
print('YNEOS'[(S_e,sum((k[1]+20*k[2])*(k[0]>0)for k in M_e))<=(S_r,sum((k[1]+20*k[2])*(k[0]>0)for k in M_r))::2],'YNEOS'[(S_e,-X)<=(S_r,-Y)::2],'YNEOS'[(S_e,min(k[1]*(k[0]>0)for k in M_e or[[0,0]]))<=(S_r,min(k[1]*(k[0]>0)for k in M_r or[[0,0]]))::2])