bus, bus2 = set(), set()
for i in range(1, 73):
    for j in range(i, 73):
        if i**3 + j**3 not in bus:
            bus.add(i**3 + j**3)
        else:
            bus2.add(i**3 + j**3)
n = int(input())
if n < 1729:
    print('none')
else:
    for k in sorted(bus2, reverse=True):
        if k <= n:
            print(k)
            break