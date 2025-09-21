import sys; input = sys.stdin.readline; from bisect import *
W = {}; H = {}
for _ in range(int(input())):
    a, b, *c = input().strip().split()
    if a>'T':
        for c in H[b]: W[c].remove(b)
        H[b].clear()
    elif a>'G':
        c = c[0]
        if b not in W: W[b] = []
        if c not in H: H[c] = []
        insort(W[b], c); H[c] += [b]
    elif W[b]: sys.stdout.write(' '.join(W[b])+'\n')
    else: sys.stdout.write('NOT FOUND\n')