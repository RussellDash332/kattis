import sys; input = sys.stdin.readline
while (n:=int(input())):
    k = input().strip().upper().replace(' ', '').replace('J', 'I'); K = []
    for i in k:
        if i not in K: K.append(i)
    for i in range(65, 91):
        if i != 74 and chr(i) not in K: K.append(chr(i))
    m = {e:i for i,e in enumerate(K)}
    for _ in range(n):
        s = [*input().strip().upper().replace(' ', '').replace('J', 'I')[::-1]]; t = []
        while s:
            if len(s) == 1: t.append(s.pop()+'X'); break
            a, b = s.pop(), s.pop()
            if a == b: s.append(b); t.append(a+'X')
            else: t.append(a+b)
        z = []
        for a, b in t:
            pa, pb = m[a], m[b]
            if a == b == 'X': z.append('YY')
            elif pa//5 != pb//5 and pa%5 != pb%5: z.append(K[5*(pa//5)+pb%5]+K[5*(pb//5)+pa%5])
            elif pa%5 == pb%5: z.append(K[5*((pa//5+1)%5)+pa%5]+K[5*((pb//5+1)%5)+pb%5])
            else: z.append(K[5*(pa//5)+(pa%5+1)%5]+K[5*(pb//5)+(pb%5+1)%5])
        print(''.join(z))
    print()