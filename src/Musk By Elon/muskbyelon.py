for x in range(int(input())):
    D = [0]*540
    for i in range(int(input())):
        s, e, *v = input().split()
        s = int(s[1:2])*60+int(s[3:5])
        e = int(e[1:2])*60+int(e[3:5])
        for t in range(s, e+1): D[t] = 1
    p = 1; s = b = 0; L = []
    for i in range(540):
        if D[i]<1:
            if p:
                if s: L += [(s, -b)]
                s = 1; b = i
            else: s += 1
        p = D[i]
    if s: L += [(s, -b)]
    d, z = max(L); z = 600-z; print(f'Day #{x+1}: Elon Musk will make Musk by Elon from {z//60}:{str(z%60).zfill(2)} for {d//60} hours and {d%60} minutes')