for _ in range(int(input())):
    s = [int(i=='T') for i in input()]; b = (-1, 0)
    for n in range(10, 0, -1):
        for p in range(n):
            if p+(n<<n) > len(s): continue
            v = [0]*(1<<n)
            for j in range(p, p+(n<<n), n):
                c = 0
                for l in range(j, j+n): c = 2*c+s[l]
                v[c] += 1 # add s[j:j+n]
            if all(v): b = max(b, (n, -p)); continue
            for j in range(p+(n<<n), len(s), n):
                if j+n > len(s): break
                # remove s[j-(n<<n):j-(n<<n)+n] and add s[j:j+n]
                c = 0
                for l in range(j-(n<<n), j-(n<<n)+n): c = 2*c+s[l]
                v[c] -= 1
                c = 0
                for l in range(j, j+n): c = 2*c+s[l]
                v[c] += 1
                if all(v): b = max(b, (n, (n<<n)-j-n)); break
        if b[0] > 0: break
    print(b[0], -b[1])