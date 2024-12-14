p, a, b, x1, y1, x2, y2 = map(int, open(0).read().split())

def d(x, y):
    try: l = (3*x*x+a)*pow(2*y, -1, p); X = l*l-2*x; return X%p, (l*(x-X)-y)%p
    except: return -1, -1

def q(x1, y1, x2, y2):
    l = (y2-y1)*pow(x2-x1, -1, p); X = l*l-x1-x2
    return X%p, (l*(x1-X)-y1)%p

if x1 == y1 == x2 == y2 == -1: print(-1, -1)
elif x1 == y1 == -1: print(x2, y2)
elif x2 == y2 == -1: print(x1, y1)
else: print(*q(x1, y1, x2, y2)) if (x1-x2)%p else print(-1, -1) if (y1-y2)%p else print(*d(x1, y1))