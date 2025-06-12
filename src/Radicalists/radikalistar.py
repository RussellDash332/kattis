import sys; input = sys.stdin.readline
n, q = map(int, input().split()); R = [{*range(1, n+1)}]; M = {i:0 for i in range(1, n+1)}; S = 1
for _ in range(q):
    c, *r = input().split()
    if c == 's': print(S)
    elif c == 'm': print(*R[M[int(r[0])]])
    else:
        _, *r = map(int, r); v = {}; k = len(R)
        for i in r:
            if M[i] not in v: v[M[i]] = len(v); R.append(set())
            R[M[i]].discard(i)
            if not R[M[i]]: S -= 1
            M[i] = v[M[i]]+k
            if not R[M[i]]: S += 1
            R[M[i]].add(i)