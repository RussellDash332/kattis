A, N, O = set(), set(), set()
for _ in range(int(input())):
    s = input().split()
    if len(s) == 1: A.add(s[0])
    else: (N if s[2] == 'and' else O).add((*sorted(s[1:-1:2]), s[-1]))
while True:
    z = 0
    for *a, b in [*N]:
        if all(x in A for x in a): A.add(b); N.discard((*a, b)); z = 1
    for *a, b in [*O]:
        if any(x in A for x in a): A.add(b); O.discard((*a, b)); z = 1
    if not z: break
print(len(A))