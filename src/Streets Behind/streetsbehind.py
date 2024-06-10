for _ in range(int(input())):
    n, k, a, b = map(int, input().split()); t = 0
    if n*(b-a)//a < 1: print(-1); continue
    while k > 0: x = n*(b-a)//a; u = (min(k, (a*x+b-1)//(b-a)-n)+x-1)//x; t += u; n += u*x; k -= u*x
    print(t)