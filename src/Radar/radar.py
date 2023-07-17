p1, p2, p3 = map(int, input().split())
x1, x2, x3 = map(int, input().split())
y1, y2, y3 = map(int, input().split())

def bezout(a, b):
    if a == 0: return 0, 1
    elif b == 0: return 1, 0
    else: p, q = bezout(b, a % b); return (q, p - q * (a // b))

s = 1e27
b1 = bezout(p1, p2)[0]
b2 = bezout(p1*p2, p3)[0]
pp = p1*p2
ppp = p1*p2*p3
for m1 in range(x1-y1, x1+y1+1, p1):
    for m2 in range(x2-y2, x2+y2+1):
        x = (m1 - p1*b1*(m1-m2)) % pp
        for m3 in range(x3-y3, x3+y3+1):
            s = min(s, (x - pp*b2*(x-m3)) % ppp)
for m1 in range(x1-y1, x1+y1+1):
    for m2 in range(x2-y2, x2+y2+1, p2):
        x = (m1 - p1*b1*(m1-m2)) % pp
        for m3 in range(x3-y3, x3+y3+1):
            s = min(s, (x - pp*b2*(x-m3)) % ppp)
for m1 in range(x1-y1, x1+y1+1):
    for m2 in range(x2-y2, x2+y2+1):
        x = (m1 - p1*b1*(m1-m2)) % pp
        for m3 in range(x3-y3, x3+y3+1, p3):
            s = min(s, (x - pp*b2*(x-m3)) % ppp)
for m1 in range(max(x1-y1, 0), x1+y1+1, p1):
    for m2 in range(x2-y2, x2+y2+1):
        x = (m1 - p1*b1*(m1-m2)) % pp
        for m3 in range(x3-y3, x3+y3+1):
            s = min(s, (x - pp*b2*(x-m3)) % ppp)
for m1 in range(x1-y1, x1+y1+1):
    for m2 in range(max(x2-y2, 0), x2+y2+1, p2):
        x = (m1 - p1*b1*(m1-m2)) % pp
        for m3 in range(x3-y3, x3+y3+1):
            s = min(s, (x - pp*b2*(x-m3)) % ppp)
for m1 in range(x1-y1, x1+y1+1):
    for m2 in range(x2-y2, x2+y2+1):
        x = (m1 - p1*b1*(m1-m2)) % pp
        for m3 in range(max(x3-y3, 0), x3+y3+1, p3):
            s = min(s, (x - pp*b2*(x-m3)) % ppp)
print(s)