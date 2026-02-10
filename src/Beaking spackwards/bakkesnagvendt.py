N = len(X:=input()); Y = input()
while N and X[N-1]==Y[N-1]: N -= 1
if N < 1: print(1); exit()
S = X[:N]+'@'+Y[:N]
M = 10**9+7; P = 31
F = [f:=1]+[f:=f*P%M for _ in range(N)]
H = [h:=1]+[h:=(h*P+ord(S[i]))%M for i in range(2*N+1)]

def get(l, r):
    return (H[r]-H[l]*F[r-l])%M
A = [n for n in range(1, N+1) if get(0, n) == get(2*N+1-n, 2*N+1)]
B = [m for m in range(1, N+1) if get(N-m, N) == get(N+1, N+m+1)]
A = A[:5]+A[-5:]; B = B[:5]+B[-5:]
for a in A:
    for b in B:
        if a+b <= N and get(a, N-b) == get(N+b+1, 2*N+1-a): print(1); exit()
print(0)