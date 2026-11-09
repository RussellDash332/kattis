tc = 0
while True:
    S = [*map(int, input().split())]
    T = sum(-~i*S[i] for i in range(10))
    if T < 1: break
    tc += 1; print(f'Box #{tc}:', end=' ')
    if T%2: print("can't be divided."); continue
    D = 1; H = T//2
    for i in range(10):
        b = 1
        while S[i]: u = min(b, S[i]); S[i] -= u; b *= 2; D |= D<<(u*-~i); D &= (1<<-~H)-1
    print('can'+"'t"*(1-(D>>H&1))+' be divided.')