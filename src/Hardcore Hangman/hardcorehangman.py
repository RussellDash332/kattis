def q(s): print('?', ''.join(chr(x+97) for x in s)); return set(map(lambda x: int(x)-1, input().split()[1:]))
N = len(q({*range(26)})); A = []; Z = ['']*N
for i in (1, 2, 4, 8, 16): A.append(q({j for j in range(26) if j&i})); A.append({*range(N)}-A[-1])
for i, e in enumerate((682, 681, 678, 677, 666, 665, 662, 661, 618, 617, 614, 613, 602, 601, 598, 597, 426, 425, 422, 421, 410, 409, 406, 405, 362, 361)):
    P = None
    for j in range(10):
        if e&(1<<j): P = A[j] if P==None else P&A[j]
    for j in P: Z[j] = chr(i+97)
print('!', ''.join(Z))