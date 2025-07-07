def f(x1, y1, r1, x2, y2, r2):
    s = (x2-x1)**2+(y2-y1)**2
    if s > (r1+r2)**2: print('impossible'); exit()
    elif s == (r1+r2)**2: return [(x1*r2+x2*r1, y1*r2+y2*r1, r1+r2)]
    elif s <= (r1-r2)**2: return (r1>r2)-(r1<r2)
    else: q = (2*(r1**2+r2**2)*s-(r1**2-r2**2)**2-s*s)**.5; v = (y1-y2, x2-x1); a = (x1+x2)*s+(r1**2-r2**2)*v[1]; b = (y1+y2)*s-(r1**2-r2**2)*v[0]; return [(a+v[0]*q, b+v[1]*q, 2*s), (a-v[0]*q, b-v[1]*q, 2*s)]
N = int(input()); C = [[*map(int, input().split())] for _ in '.'*N]; I = [0]*N; O = [0]*N; V = {}
for i in range(N):
    for j in range(i+1, N):
        v = f(*C[i], *C[j])
        if v == 1: I[j] += 1; O[i] += 1
        if v == -1: I[i] += 1; O[j] += 1
        if O[i] or O[j]: continue
        if type(v) == list:
            for p, q, c in v:
                ok = 1
                for k in range(N):
                    if k == i or k == j: continue
                    x, y, r = C[k]
                    if (p-c*x)**2 + (q-c*y)**2 > r*r*c*c: ok = 0; break
                if not ok: continue
                k = (p/c, q/c)
                if k not in V: V[k] = set()
                V[k].add(i); V[k].add(j)
if max(I) == N-1: print('voter', I.index(N-1)+1); exit()
for p in [*V]: V[p] = sorted(x+1 for x in V[p] if not O[x])
if not V: print('impossible'); exit()
print('compromise', len(V))
for h in sorted(V, key=lambda x: V[x]): print(*h, *V[h])