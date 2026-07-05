import sys; input = sys.stdin.readline; print = sys.stdout.write; from bisect import *
B = [[]]; N = int(input())
for _ in range(N):
    i = input()
    if i[0] == '0': continue
    i = int(i)
    for b in B:
        p = bisect(b, i)
        if p == len(b): b.append(i); break
        else: i, b[p] = b[p], i
    else: B.append([i])
for b in B: print(' '.join(map(str, b))); print(';\n')