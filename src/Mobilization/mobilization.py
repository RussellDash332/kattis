import sys; input = sys.stdin.readline
n, X = map(int, input().split()); P = []; Z = 0
for _ in range(n): c, a, b = map(float, input().split()); P.append((a*X/c, b*X/c))
P.sort(reverse=True); Q = [P[0]]
for i in range(1, n):
    if P[i][1] > Q[-1][1]: Q.append(P[i])
for i in range(min(2, len(Q))):
    a, b = Q[i]
    for j in range(i+1, len(Q)):
        c, d = Q[j]; A = 4*(e:=c-a)*(f:=b-d); B = f*c-e*d
        if 0<2*B<A: Z = max(Z, c*d+B*B/A)
print(max(Z, *(a*b for a,b in P)))