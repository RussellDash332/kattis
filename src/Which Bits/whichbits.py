H = {}; Z = []
def q(a, b):
    if (a, b) not in H: print('q', a, b); H[(a, b)] = int(input())
    return H[(a, b)]
def f(a, b):
    if a == b: return Z.append(a)
    s = q(a, b)
    if s == 0: return
    l = q(a, mi:=(a+b)//2); H[(mi+1, b)] = s-l
    if s == l: f(a, mi)
    elif l == 0: f(mi+1, b)
    else: f(a, mi); f(mi+1, b)
f(0, 2**63-1); print('a', len(Z), *Z)