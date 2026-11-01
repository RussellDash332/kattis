MOD = 998244353
n, m, k = map(int, input().split()); K = 0
P = sum(input().count('#') for _ in range(n))
if P == 0: print(1); exit()
for _ in range(k): r, g, b = map(int, input().split()); K += r+g+b<384
F = [f:=1]+[f:=f*-~i%MOD for i in range(P)]
I = [f:=pow(f, -1, MOD)]+[f:=f*(P-i)%MOD for i in range(P)]
B = [k:=1]+[k:=k*K%MOD for i in range(P)]
print(sum(F[P]*I[~(P-s)]*B[s] for s in range(P%2, P+1, 2))%MOD)