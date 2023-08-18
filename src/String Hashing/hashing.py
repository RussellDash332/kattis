s, n = input().strip(), int(input())
h, p, f, m = [ord(s[0])-95], 31, 1, 10**18 + 7
for i in range(1, len(s)):
    f *= p; f %= m
    h.append((h[-1] + f*(ord(s[i])-95))%m)
h.append(0)
for _ in range(n):
    i, j = map(int, input().split())
    print(((h[j-1]-h[i-1])*pow(pow(p, i, m), -1, m)) % m)