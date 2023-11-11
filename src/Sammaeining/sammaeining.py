def mult(p1, p2):
    p = [0]*(len(p1)+len(p2)-1)
    for i in range(len(p1)):
        for j in range(len(p2)): p[i+j] += p1[i]*p2[j]
    return p

def polypow(p, n):
    if n == 1: return p
    elif n % 2 == 1:
        p2 = mult(p, polypow(p, n-1))
        return [sum(p2[i] for i in range(len(p2)) if i%10==j)%MOD for j in range(10)]
    p2 = mult(p, p)
    return polypow([sum(p2[i] for i in range(len(p2)) if i%10==j)%MOD for j in range(10)], n//2)

n = int(input()); MOD = 10**9+7
p = [1]
for i in range(1, 11):
    p = mult(p, [1, *[0]*(i-1), 1])
    if i == n: print(sum(p[i] for i in range(len(p)) if i%10==7)), exit(0)
p = [sum(p[i] for i in range(len(p)) if i%10==j) for j in range(10)]
t, r = divmod(n, 10); p = polypow(p, t)
for i in range(1, r+1): p = mult(p, [1, *[0]*(i-1), 1])
print(sum(p[i] for i in range(len(p)) if i%10==7)%MOD)