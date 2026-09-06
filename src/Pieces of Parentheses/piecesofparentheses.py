N = int(input())
B = []
for _ in range(N):
    S = []; L = len(s:=input())
    for i in s:
        if not S or i != ')' or S[-1] != '(': S.append(i)
        else: S.pop()
    B += [(S.count('('), S.count(')'), L)]
B.sort(key=lambda x: (s:=x[0]<x[1], (x[1], -x[0])[s]))
D = [-1]*10**5; D[0] = 0
for o, c, l in B:
    x = o-c
    for b in (range(len(D)-1-x, c-1, -1) if x >= 0 else range(c, len(D))):
        if ~D[b] and D[b]+l > D[b+x]: D[b+x] = D[b]+l
print(D[0])