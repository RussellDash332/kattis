from math import *
def solve():
    m, n, p, q = map(int, input().split())

    if m == n:
        if len(str(p*q)) != m: print('IMPOSSIBLE')
        else: print(p*q)
        return

    base = str(p*q%10**(k:=len(sp:=str(p)))).zfill(k)
    if int(k+log10(q)) not in [n-1, n, n+1]: return print('IMPOSSIBLE')
    carry = (p*q-int(base))//10**k

    left = ['-1']*m
    right = ['-1']*m
    for i in range(len(base)): right[-i-1] = base[-i-1]
    for i in range(k): left.append(sp[i])

    k2 = k
    while k2 <= m-k:
        cut = 0
        for i in range(k-1, -1, -1):
            if m-k2+i == n-1: cut = 1; break
            left[m-k2+i] = right[m-k2+i]
        if cut: break
        tmp2 = int(''.join(right[m-k2:m-k2+k]))*q+carry
        tmp, carry = str(tmp2%10**k).zfill(k), tmp2//10**k
        for i in range(k): right[m-k-k2+i] = tmp[i]
        k2 += k

    if right[0] == '0': return print('IMPOSSIBLE')
    cp = [int(i) for i in left]; carry = 0
    i = len(left)-1
    while i > n-1: cp[i] *= q; cp[i] += carry; carry = cp[i]//10; cp[i]%=10; i -= 1
    while carry and i >= 0: cp[i] = carry%10; carry //= 10; i -= 1
    if carry: return print('IMPOSSIBLE')
    pos = -1
    for _ in range(m):
        if right[pos] == '-1': right[pos] = str(cp[pos])
        if cp[pos] != int(right[pos]): return print('IMPOSSIBLE')
        pos -= 1
    for p in range(pos, -len(cp)-1, -1):
        if cp[p] != -1: return print('IMPOSSIBLE')
    if right[0] == '0' or right[0] == '-1': return print('IMPOSSIBLE')
    return print(''.join(right))

'''
5 2 8 4
2 1 11 4
3 1 10 10
100 2 8 4
20 2 88 4
1000000 2 8 4
'''
solve()