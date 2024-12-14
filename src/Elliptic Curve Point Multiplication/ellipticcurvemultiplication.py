p, a, b, n, x2, y2 = map(int, open(0).read().split())

def d(x, y):
    try: l = (3*x*x+a)*pow(2*y, -1, p); X = l*l-2*x; return X%p, (l*(x-X)-y)%p
    except: return -1, -1

def q(x1, y1, x2, y2):
    l = (y2-y1)*pow(x2-x1, -1, p); X = l*l-x1-x2
    return X%p, (l*(x1-X)-y1)%p

def c(x1, y1, x2, y2):
    if x1 == y1 == x2 == y2 == -1: return -1, -1
    if x1 == y1 == -1: return x2, y2
    if x2 == y2 == -1: return x1, y1
    return q(x1, y1, x2, y2) if (x1-x2)%p else (-1, -1) if (y1-y2)%p else d(x1, y1)

x = y = -1
for i in bin(n)[:1:-1]:
    if i>'0': x, y = c(x, y, x2, y2)
    x2, y2 = c(x2, y2, x2, y2)
print(x, y)