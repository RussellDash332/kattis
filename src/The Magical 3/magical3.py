import sys
for line in sys.stdin:
    n = int(line)-3
    if n == -3: break
    if n < 0:
        print('No such base')
        continue
    if n == 0:
        print(4)
        continue
    d = 4e9
    for i in range(4, int(n**0.5)+4):
        if n%i == 0:
            d = i
            break
    for t in range(1, 4):
        if n%t == 0 and n//t >= 4: d = min(d, n//t)
    if d == 4e9: print('No such base')
    else: print(d)