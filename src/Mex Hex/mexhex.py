N, D, *P = map(int, open(0).read().split()); I = {}
for i in range(N):
    if P[i] not in I: I[P[i]] = []
    I[P[i]] += [i]
for x in range(N+1):
    if x not in I: print(x); break
    t = I[x]; z = l = r = 0; G = -D-1
    while l < len(t):
        while r < len(t) and t[r] < t[l]+D: r += 1
        if t[l]+D <= (u:=max(t[r-1], G+2*D)): z = 1; break
        G = u; l = r
    if 1-z: print(x); break