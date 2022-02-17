x = int(float(input()) * 10**4)

if x >= 10**5:
    print('No solution')
else:
    arr = []
    for n in range(8):
        for a0 in range(1, 10):
            a = (10**(n + 5) - 10**4) * a0 / (10**5 - x)
            a2 = (10**(n + 5) - 10**4) * a0 // (10**5 - x)
            if a // 10**n == a0 and a == a2:
                arr.append(a2)
    arr.sort()
    if arr:
        for i in arr:
            print(i)
    else:
        print('No solution')