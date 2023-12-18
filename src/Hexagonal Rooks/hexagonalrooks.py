s, t = input().split(); v = {}; x = 'abcdefghijk'
for i, e in enumerate([x]*6+[x[j+1:-j-1] for j in range(5)]): v.update({l+str(i+1):set() for l in e})
def pos(s): return (ord(s[0])-ord('a'), int(s[1:])-1)
for i in v:
    for j in v:
        if i == j: continue
        (ci, ri), (cj, rj) = pos(i), pos(j)
        if ci == cj or (ci-ri == cj-rj and ci <= 5 and cj <= 5) or (ci+ri == cj+rj and ci >= 5 and cj >= 5) or (ci <= 5 and cj >= 5 and (5-ci+ri == rj)|(rj+cj == ri+5)) or (ri == rj and (ci >= 5 and cj >= 5)|(ci <= 5 and cj <= 5)): v[i].add(j), v[j].add(i)
print(sum(i in v[s] and t in v[i] for i in v))