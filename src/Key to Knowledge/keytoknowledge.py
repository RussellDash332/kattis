import sys; input = sys.stdin.readline
P = [1<<i for i in range(30)]
for _ in range(int(input())):
    n, m = map(int, input().split()); B = []; C = []; H = {}; S = None; U = 1
    for _ in range(n): b, c = input().split(); B.append(int(b, 2)); C.append(int(c))
    for bm in range(1<<(m//2)):
        z = []
        for i in range(n):
            c = 0
            for j in range(m//2): c += bool(bm&P[j])==bool(B[i]&P[j])
            z.append(c)
        z = tuple(z)
        if z not in H: H[z] = []
        H[z].append(bm)
    for bm in range(1<<(m-m//2)):
        z = []
        for i in range(n):
            c = 0
            for j in range(m-m//2): c += bool(bm&P[j])==bool(B[i]&P[j+m//2])
            z.append(c)
        d = tuple(C[i]-z[i] for i in range(n))
        if d not in H: continue
        if S == None and len(H[d]) == 1: S = (bm<<(m//2))+H[d][0]
        elif U: S = (S!=None)+len(H[d]); U = 0
        else: S += len(H[d])
    if S == None: print('0 solutions')
    elif U: print(bin(S)[2:].zfill(m))
    else: print(S, 'solutions')