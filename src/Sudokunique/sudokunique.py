from array import *; P = {1<<i:i for i in range(10)}; E = [1<<i for i in range(10)]; BC = array('b', (bin(i).count('1') for i in range(1023)))

def solve(m):
    sol = [None]; V = [1022]*81; R = [1022]*9; C = [1022]*9; B = [1022]*9
    for r in range(9):
        for c in range(9):
            if (v:=E[m[9*r+c]]) > 1:
                if R[r]&v and C[c]&v and B[3*(r//3)+c//3]&v: R[r] ^= v; C[c] ^= v; B[3*(r//3)+c//3] ^= v
                else: return print('Find another job')
    for r in range(9):
        for c in range(9):
            if (x:=m[9*r+c]):
                for i in range(9): V[y] = (V[y:=9*i+c]|E[x])^E[x]; V[y] = (V[y:=9*r+i]|E[x])^E[x]
                for i in range(3):
                    for j in range(3): V[y] = (V[y:=9*(r//3*3+i)+c//3*3+j]|E[x])^E[x]
                V[9*r+c] = 0
    def bt(s):
        if not s:
            if sol[0] != None and sol[0] != m: 1/0
            elif sol[0] == None: sol[0] = [*m]
            return
        rc = min(s, key=lambda x: BC[V[x]]); s.discard(rc); bm = V[rc]; r, c = divmod(rc, 9)
        while bm:
            v = bm&-bm; bm ^= v; m[rc] = P[v]; rm = [rc]; V[rc] ^= v
            for i in range(9):
                if v&V[9*i+c]: rm.append(9*i+c); V[9*i+c] ^= v
                if v&V[9*r+i]: rm.append(9*r+i); V[9*r+i] ^= v
            for i in range(3):
                for j in range(3):
                    if v&V[9*(r//3*3+i)+c//3*3+j]: rm.append(9*(r//3*3+i)+c//3*3+j); V[9*(r//3*3+i)+c//3*3+j] ^= v
            bt(s)
            for x in rm: V[x] |= v
        s.add(rc)
    try: bt({i for i in range(81) if m[i]==0})
    except: return print('Non-unique')
    if sol[0] == None: return print('Find another job')
    print(*sol[0])

import sys; input = sys.stdin.readline
while 1:
    m = []
    for _ in range(9): m.extend(map(int, input().split()))
    input()
    if not m: break
    solve(m)