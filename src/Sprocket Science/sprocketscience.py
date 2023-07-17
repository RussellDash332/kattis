def gcd(a, b):
    while b: a, b = b, a%b
    return a
def lcm(a, b):
    return a*b//gcd(a, b)

frac = [[*map(int, input().split('/'))] for _ in range(12)]
for i in range(4097):
    if (b:=bin(i)).count('1') != 6: continue
    left, right = [], []
    for k, j in enumerate(b[2:].zfill(12)):
        if j == '1': left.append(frac[k])
        else: right.append(frac[k])
    llcm = rlcm = 1
    for a, b in left: llcm = lcm(llcm, a)
    for a, b in right: rlcm = lcm(rlcm, a)
    for i in range(6): left[i], right[i] = [llcm, llcm//left[i][0]*left[i][1]], [rlcm, rlcm//right[i][0]*right[i][1]]
    ldenoms = sorted(i[1] for i in left)
    lgcd = llcm
    for i in range(6): lgcd = gcd(lgcd, ldenoms[i])
    llcm //= lgcd; ldenoms = [i//lgcd for i in ldenoms]
    rdenoms = sorted(i[1] for i in right)
    rgcd = rlcm
    for i in range(6): rgcd = gcd(rgcd, rdenoms[i])
    rlcm //= rgcd; rdenoms = [i//rgcd for i in rdenoms]
    cross = {ldenoms[i]*rdenoms[(i+1)%6]-ldenoms[(i+1)%6]*rdenoms[i] for i in range(6)}
    if cross == {0}:
        if ldenoms[0] < rdenoms[0]:
            ratio = [rdenoms[0], ldenoms[0]]
            for i in range(6): ldenoms[i] = ldenoms[i]*ratio[0]//ratio[1]
            llcm = llcm*ratio[0]//ratio[1]
        elif ldenoms[0] > rdenoms[0]:
            ratio = [ldenoms[0], rdenoms[0]]
            for i in range(6): rdenoms[i] = rdenoms[i]*ratio[0]//ratio[1]
            rlcm = rlcm*ratio[0]//ratio[1]
        d = gcd(llcm, rlcm)
        for i in ldenoms: d = gcd(d, i)
        for i in rdenoms: d = gcd(d, i)
        llcm //= d; rlcm //= d; ldenoms = [i//d for i in ldenoms]
        print(llcm, rlcm), print(*ldenoms), exit(0)
print('impossible')