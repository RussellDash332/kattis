from bisect import *
N, L = map(int, input().split()); H = {}; Q = []
for t in range(1, L+1):
    c, a, b = input().split(); a = int(a); b = int(b)
    if a > b: a, b = b, a
    if c != 'QUERY':
        if (a, b) not in H: H[(a, b)] = []
        H[(a, b)].append(t if c == 'ADD' else -t)
    else: Q += [(a, b, t)]
for a, b, t in Q:
    if (a, b) not in H: print('unsure')
    else:
        t = bisect(h:=H[(a, b)], t, key=abs)
        if t < len(h): print('un'*(h[t]>0)+'safe')
        else: print('un'*(h[-1]<0)+'safe')