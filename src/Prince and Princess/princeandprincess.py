import sys; input = sys.stdin.readline; from bisect import *
def lis(A):
    B = []
    for e in A:
        p = bisect(B, e-1)
        if p == len(B): B.append(e)
        else: B[p] = e
    return len(B)
for tc in range(int(input())):
    n, p, q = map(int, input().split())
    a, b = [*map(int, input().split())], [*map(int, input().split())]
    c = []; r = {e:i for i,e in enumerate(a)}
    for i in range(q+1):
        if b[i] in r: c.append(r[b[i]])
    print(f'Case {tc+1}: {lis(c)}')