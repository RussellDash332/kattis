import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**5)
n = int(input()); M1 = 10**18+7; M2 = 10**9+3233

def trav(t, h):
    if type(t) == int:
        return (pow(2, t, M1), pow(2, t, M2))
    else:
        a = trav(t[0], h); b = trav(t[1], h); h.add(a); h.add(b)
        return ((a[0]+b[0])%M1, (a[1]+b[1])%M2)

ha = set(); hb = set()
ha.add(trav(eval(input()), ha))
hb.add(trav(eval(input()), hb))
print(len(ha&hb))