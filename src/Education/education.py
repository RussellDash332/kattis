N, M = map(int, input().split())
S = sorted((-e, i) for i, e in enumerate(map(int, input().split())))
B = [(c, p, i+1) for i, (c, p) in enumerate(zip(map(int, input().split()), map(int, input().split())))]
Z = [-1]*N
for ne, i in S:
    z = min([(p, i, c) for c, p, i in B if c>=-ne], default=-1)
    if z != -1: Z[i] = z[1]; B.remove((z[2], z[0], z[1]))
print(*(Z if -1 not in Z else ['impossible']))