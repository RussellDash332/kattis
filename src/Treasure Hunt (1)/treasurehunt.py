m = open(0).readlines()[1:]
r, c, R, C = 0, 0, len(m), len(m[0].strip())
v = set()
t = 0
while True:
    d = m[r][c]
    if d == 'N':    r -= 1
    elif d == 'S':  r += 1
    elif d == 'W':  c -= 1
    elif d == 'E':  c += 1
    if d == 'T': print(t); break
    t += 1
    if not (0<=r<R and 0<=c<C): print('Out'); break
    if (r, c) in v: print('Lost'); break
    v.add((r, c))