tc = 0
while True:
    S = [*map(int, input().split())]
    T = sum(-~i*S[i] for i in range(10))
    if T < 1: break
    tc += 1; print(f'Box #{tc}:')
    if T%2: print("Can't be divided."); continue
    D = [0]*-~T; D[0] = 1
    for i in range(10):
        b = 1
        while S[i]:
            u = min(b, S[i]); S[i] -= u; b *= 2
            for v in range(T+u*~i, -1, -1): D[v-u*~i] |= D[v]
    print('Can'+"'t"*(1-D[T//2])+' be divided.')