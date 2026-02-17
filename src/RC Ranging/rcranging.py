x = y = dx = 0; dy = 1; F = {}
L = open(0).read().split(); N = len(L); p = -1
def parse():
    global p
    c = L[p:=p+1]
    if c == 'FORWARD': v = int(L[p:=p+1]); return (c, v)
    elif c == 'LEFT': return (c,)
    elif c == 'RIGHT': return (c,)
    elif c == 'DO':
        return F[L[p:=p+1]]
    elif c == 'TO':
        f = L[p:=p+1]; z = []
        while 1:
            t = parse()
            if not t: break
            z.append(t)
        F[f] = z
    elif c == 'REPEAT':
        v = int(L[p:=p+1]); z = []
        while 1:
            t = parse()
            if not t: break
            z.append(t)
        return [z for _ in range(v)]
    return []
def process(Z):
    global x, y, dx, dy
    if not Z: return
    if Z[0] == 'FORWARD': k = Z[1]; x += k*dx; y += k*dy
    elif Z[0] == 'LEFT': dx, dy = -dy, dx
    elif Z[0] == 'RIGHT': dx, dy = dy, -dx
    else:
        for u in Z: process(u)
Z = []
while p+1 < N: Z.append(parse())
process(Z)
print(x, y)