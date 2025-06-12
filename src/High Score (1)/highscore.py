for _ in range(int(input())):
    s = [*map(lambda x: min(ord(x)-65, 91-ord(x)), input())]; n = len(s); z = 10**9
    p = [i for i in range(n) if s[i] or i == 0]; u = len(p)
    for i in range(u): z = min(z, p[i]+(p[i]-p[(i+1)%u])%n, (-p[i])%n+(p[(i-1)%u]-p[i])%n)
    print(z+sum(s))