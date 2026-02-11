from array import *
n = int(input()); P = [complex(*map(int, input().split())) for _ in range(n)]; D = array('f', [abs(P[i>>8]-P[i%256] if i%256 < n else 0) for i in range(n<<8)])
Z = array('f', [1e9]*n); q1 = array('h', [-1]*~-n); p2 = array('f', [0]*~-n); t1 = array('h', [-1]*~-n); s2 = array('f', [0]*~-n)
G = lambda a, b: max(2*a, 2*b, a+d+b)
for c in range(n):
    m1 = m2 = 0; m = -1
    for r in range(n):
        if r-c:
            if (d:=D[c<<8|r]) > m1: m1, m2, m = d, m1, r
            elif d > m2: m2 = d
    for r in range(n):
        if r-c and Z[r] > (d:=2*(m1 if r-m else m2)): Z[r] = d
for u in range(n):
    for v in range(u):
        for i in range(~-n): q1[i] = t1[i] = -1; p2[i] = s2[i] = 0
        L = sorted((x for x in range(n) if x-u and x-v), key=lambda x: D[u<<8|x]-D[v<<8|x]); d = D[u<<8|v]; M = 1e9
        for i in range(n-2): q1[i+1], p2[i+1] = (L[i], b) if (a:=D[u<<8|L[i]]) > (b:=D[u<<8|q1[i]]) else (q1[i], max(p2[i], a)); t1[~i-1], s2[~i-1] = (L[~i], b) if (a:=D[v<<8|L[~i]]) > (b:=D[v<<8|t1[~i]]) else (t1[~i], max(s2[~i], a))
        for k in range(~-n):
            if M > (x:=G(D[u<<8|q1[k]], D[v<<8|t1[k]])): M = x
        for r in L:
            if Z[r] > M: Z[r] = M
        for k in range(~-n):
            pu = q1[k]; sv = t1[k]
            if ~pu and Z[pu] > (r:=G(p2[k], D[v<<8|t1[k]])): Z[pu] = r
            if ~sv and Z[sv] > (r:=G(D[u<<8|q1[k]], s2[k])): Z[sv] = r
print(int(P[p:=min(range(n), key=lambda x: Z[x])].real), int(P[p].imag), Z[p])