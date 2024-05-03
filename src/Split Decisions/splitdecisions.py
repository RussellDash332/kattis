n = int(input()); W = [input().strip() for _ in range(n)]; H = {}
for i in range(n):
    for j in range(i+1, n):
        if len(W[i]) != len(W[j]): continue
        d = None; e = 0
        for k in range(len(W[i])): e += W[i][k] != W[j][k]
        if e != 2: continue
        for k in range(len(W[i])-1):
            if W[i][k] != W[j][k] and W[i][k+1] != W[j][k+1]:
                if d: d = None; break
                d = (k, len(W[i]), *sorted([W[i][k:k+2], W[j][k:k+2]]))
        if d:
            if d not in H: H[d] = 0
            H[d] += 1
print(sum(i==1 for i in H.values()))