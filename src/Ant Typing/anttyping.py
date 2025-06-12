from itertools import *
s = input(); h = [0]*81; t = int(s[0])-1; Z = 10**9
for i in range(len(s)-1): h[9*int(s[i])+int(s[i+1])-10] += 1
for p in permutations(range(9)):
    z = p[t]
    for i in range(81): z += abs(p[i//9]-p[i%9])*h[i]
    Z = min(z, Z)
print(Z+len(s))