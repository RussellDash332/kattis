N, H = map(int, input().split()); G = {'Power': {}, 'Ground': {}}
for _ in range(N):
    p1, p2 = input().split()
    p1, *n1 = p1.split('-'); n1 = n1[0] if n1 else ''
    p2, *n2 = p2.split('-'); n2 = n2[0] if n2 else ''
    if p1 not in G: G[p1] = {}
    if n1 not in G[p1]: G[p1][n1] = []
    if p2 not in G: G[p2] = {}
    if n2 not in G[p2]: G[p2][n2] = []
    G[p1][n1] += [(p2, n2)]; G[p2][n2] += [(p1, n1)]
print(f'Need {len(G["Power"][""])} holes on power rail')
print(f'Need {len(G["Ground"][""])} holes on ground rail')
V = {'Power-', 'Ground-'}; Z = 0
for i in G:
    for p in G[i]:
        if i+'-'+p not in V:
            q = [i+'-'+p]; V.add(q[0])
            for u in q:
                u, u2 = u.split('-')
                for v, v2 in G[u][u2]:
                    if v+'-'+v2 not in V: q += [v+'-'+v2]; V.add(q[-1]) 
            if len(q) > 1: Z += max((len(q)-3)//(H-2), 0)+1
print(f'Need {Z} additional {H}-hole groups')
for p in sorted(G, key=lambda x: (''.join(i for i in x if i.isalpha()), int(''.join(i for i in x if i.isdigit()) or '0'))):
    if p not in ('Power', 'Ground'): print(f'Part {p} has {len(G[p])} pins')