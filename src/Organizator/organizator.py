n, *a = map(int, open(0).read().split()); M = [0]*(max(a)+1); Z = 0
for i in a: M[i] += 1
for i in range(1, max(a)+1):
    z = sum(M[i::i])
    if z > 1: Z = max(Z, z*i)
print(Z)