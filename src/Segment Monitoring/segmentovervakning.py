import sys; input = sys.stdin.readline; from heapq import *; from array import *
xmin, xmax = map(int, input().split()); C = array('i'); L = []; H = []; D = array('b', [0]*(N:=10**6+1)); M = 10**9+7
for _ in range(int(input())):
    t, *r = input().split()
    if t < '-':
        s, lo, hi = map(int, r)
        if lo <= xmin and xmax <= hi: C.append(s)
        elif lo <= xmin: heappush(L, (M-hi)*N+s)
        elif xmax <= hi: heappush(H, lo*N+s)
    else:
        D[int(r[0])] = 1 # lazy deletion
        while C and D[C[-1]]: C.pop()
        while L and D[L[0]%N]: heappop(L)
        while H and D[H[0]%N]: heappop(H)
    if C: print(1)
    elif L and H and L[0]//N+H[0]//N <= M: print(2)
    else: print(-1)