import sys; input = sys.stdin.readline; from bisect import *
H = [[] for _ in range(1001)]; C = [None]*1001; M = [{} for _ in range(1001)]
for _ in range(int(input())):
    d, c, *r = input().split(); d = int(d)
    if c == 'a':   H[d] = [*H[k:=int(r[0])]]; M[d] = {**M[k]}; C[d] = None
    elif c == '?': x = int(r[0]); C[d] = x if x in M[d] else None
    elif c == 'l': b = bisect_left(H[d], int(r[0])); C[d] = H[d][b] if 0 <= b < len(H[d]) else None
    elif c == 'u': b = bisect(H[d], int(r[0])); C[d] = H[d][b] if 0 <= b < len(H[d]) else None
    elif c == 'i':
        k, v = map(int, r); C[d] = k
        if k not in M[d]: insort(H[d], k); M[d][k] = v
    elif c == 'e':
        k = C[d]
        if k != None: H[d].remove(k); M[d].pop(k); C[d] = None
    elif c == 'f': C[d] = H[d][0] if H[d] else None
    elif c == 'b': C[d] = H[d][-1] if H[d] else None
    elif c == '>':
        if C[d] != None: b = bisect(H[d], C[d]); C[d] = H[d][b] if 0 <= b < len(H[d]) else None
    elif c == '<':
        if C[d] != None: b = bisect_left(H[d], C[d])-1; C[d] = H[d][b] if 0 <= b < len(H[d]) else None
    elif c == 'r': print(bisect_left(H[d], C[d]) if C[d] in M[d] else '-')
    elif c == 'k': C[d] = H[d][int(r[0])]
    elif c == 'g': print(M[d][C[d]] if C[d] in M[d] else '-')
    elif c == 's':
        if C[d] != None: M[d][C[d]] = int(r[0])
    else: print(len(H[d]))