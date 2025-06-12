from functools import *
@cache
def ask(s): print('?', s); return int(input())
N, K = map(int, input().split()); V = [ask(chr(97+i)*N) for i in range(K-1)]; V.append(N-sum(V)); s = 'a'*V[0]; V[0] = p = 0
while len(s) != N:
    while V[p] == 0: p += 1
    lo, hi = 0, len(s); ch = chr(97+p)*V[p]
    while hi-lo>1:
        mi = (lo+hi)//2
        if ask(s[:mi]+ch) == mi+V[p]: lo = mi
        else: hi = mi-1
    v = hi if ask(s[:hi]+ch) == hi+V[p] else hi-1; s = s[:v]+chr(97+p)+s[v:]; V[p] -= 1
print('!', s)