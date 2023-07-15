import sys; input = sys.stdin.readline
from collections import defaultdict
sup = lambda: defaultdict(int)

def pow(mat, n):
    if n == 0:
        i = defaultdict(sup)
        for j in range(k+1): i[j][j] = 1
        return i
    if n == 1: return mat
    if n % 2: return mul(pow(mat, n-1), mat)
    return pow(mul(mat, mat), n//2)

def mul(a, b):
    c = defaultdict(sup)
    for i in a:
        for k in a[i]:
            if k not in b: continue
            for j in b[k]: c[i][j] += a[i][k]*b[k][j]; c[i][j] %= (1<<32)
    return c

# helper tools
def densify(sm):
    m = [[0]*(k+1) for _ in range(k+1)]
    for i in sm:
        for j in sm[i]: m[i][j] = sm[i][j]
    return m
def numerate(stack):
    r = []
    for i in stack:
        if type(i) != list: r.append(len(i))
        else: r.append(numerate(i))
    return r

n, k = map(int, input().split())
v = {i:{0:e} for i,e in enumerate(map(int, input().split()))}; v[k] = {0:1}
ptrs, stack = [], [[]]
ptrs.append(stack[0])
mat = defaultdict(sup)
mults = [1]
for cmd in ['for 1', *sys.stdin, 'rof']:
    q, *r = cmd.replace(',', '').split()
    if q == 'add': # first = second + third
        a, b, c = int(r[0][1:]), int(r[1][1:]), int(r[2][1:])
        for i in range(k+1): mat[i][i] = 1
        mat[a][a] = 0; mat[a][b] += 1; mat[a][c] += 1
        ptrs[-1].append(mat); mat = defaultdict(sup)
    elif q == 'addi': # first = second + thirdc
        a, b, c = int(r[0][1:]), int(r[1][1:]), int(r[2])
        for i in range(k+1): mat[i][i] = 1
        mat[a][a] = 0; mat[a][b], mat[a][k] = 1, c
        ptrs[-1].append(mat); mat = defaultdict(sup)
    elif q == 'li': # first = secondc
        a, c = int(r[0][1:]), int(r[1])
        for i in range(k+1): mat[i][i] = 1
        mat[a][a] = 0; mat[a][k] = c
        ptrs[-1].append(mat); mat = defaultdict(sup)
    elif q == 'move': # first = second
        a, b = int(r[0][1:]), int(r[1][1:])
        if a == b: continue
        for i in range(k+1): mat[i][i] = 1
        mat[a][a] = 0; mat[a][b] = 1
        ptrs[-1].append(mat); mat = defaultdict(sup)
    elif q == 'for': # for loop
        a = int(r[0])
        ptrs[-1].append([]), ptrs.append(ptrs[-1][-1]), mults.append(a)
    elif q == 'rof': # end loop
        curr = ptrs.pop()
        if not curr or mults[-1] == 0: ptrs[-1].pop(), mults.pop(); continue
        mat = curr[0]
        for i in range(1, len(curr)): mat = mul(curr[i], mat)
        ptrs[-1].pop(), ptrs[-1].append(pow(mat, mults.pop())); mat = defaultdict(sup)
res = mul(stack[0][0], v)
print(*(res[i][0] for i in range(k)))