n, k = map(int, input().split())
if n < k or n >= 1<<k: print('impossible'); exit()
T = [1]*k
for i in range(l:=min(64, k)): T[i] = 1<<i
U = (1<<l)-1+max(0, k-l)
for i in range(l-1, -1, -1): u = min(U-n, T[i]-1); T[i] -= u; U -= u
W = (2*n+1).bit_length()
L = [(d, i) for d, c in enumerate(T) for i in range(c)]
Z = [0]*n
for r, i in enumerate(sorted(range(n), key=lambda x: ((b:=(2*L[x][1]+1).bit_length())-L[x][0],(2*L[x][1]+1)<<(W-b)))): Z[i] = r+1
print(*Z)