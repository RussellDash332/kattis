from itertools import *
S = set(); V = 'aeiou'; C = 'bcdfghjklmnpqrstvwxyz'
for v1 in range(5):
    for v2 in range(5):
        for c1 in range(21): c2 = -(v1+v2+c1)%21; S |= {''.join(w) for w in permutations(V[v1]+V[v2]+C[c1]+C[c2])}
print(len(S), *S)