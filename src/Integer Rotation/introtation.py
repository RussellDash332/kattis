M = 10**6; m = [0]*M; E = [10**i for i in range(7)]
for l in range(6):
    for v in range(E[l], E[l+1]):
        r = s = v
        for _ in range(l):
            if r > (t:=(v%10)*E[l]+v//10) and v%10: r = t
            v = t
        m[s] = r
z = [[] for _ in range(M)]
for i in range(M): z[m[i]].append(i)
P = [x for x in z if x]
for _ in range(int(input())):
    a, b = map(int, input().split()); c = 0
    for p in P:
        k = 0
        for t in p: # linear pass with early termination works but not binary search? lmao constant factor things
            if t > b: break
            k += a <= t
        c += k*(k-1)
    print(c//2)