import sys; input = sys.stdin.readline; print = sys.stdout.write
Z = ['Svindl\n', 'Raunhaeft\n']
for _ in range(int(input())):
    C = 0; P = {}; N = {}; Pe = {}; Ne = {}; S = (input().strip()+'+0').replace('d1-', '-').replace('d1+', '+')
    for s in S.split('+'):
        t = s.split('-'); u = t[0] == ''
        if 'd' in t[u]:
            n, m = t[u].split('d'); n = int(n)
            if t[u][-1] == '!': D = (Pe, Ne)[u]; m = int(m[:-1])
            else: D = (P, N)[u]; m = int(m)
            if m not in D: D[m] = 0
            D[m] += n
        else: C += (1-2*u)*int(t[u])
        for v in t[u+1:]:
            if 'd' in v:
                n, m = v.split('d'); n = int(n)
                if v[-1] == '!': D = Ne; m = int(m[:-1])
                else: D = N; m = int(m)
                if m not in D: D[m] = 0
                D[m] += n
            else: C -= int(v)
    L = R = C
    for k, v in P.items(): L += v; R += k*v
    for k, v in N.items(): L -= k*v; R -= v
    x = int(input()); spe = sum(Pe.values()); sne = sum(Ne.values())
    if spe: R = 10**36
    if sne: L = -10**36
    for k, v in Pe.items(): L += v
    for k, v in Ne.items(): R -= v
    if (k:={*[*Pe], *[*Ne]}) == {2}: print(Z[L<=x<=R and (x-C)%2==(spe+sne)%2])
    elif spe+sne == 1: K = k.pop(); print(Z[L<=x<=R and (x-C)%K>0])
    else: print(Z[L<=x<=R])