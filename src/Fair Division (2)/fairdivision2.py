n, m = map(int, input().split())
wN = [0, 1]
for q in range(2, int(m**(1/(n-1)))+1):
    wN.append(q**n)
    for p in range(1, q):
        a, b = m*p, wN[q]-wN[q-p]
        if a % b == 0: print(p, q), exit(0)
print('impossible')