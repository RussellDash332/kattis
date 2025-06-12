def syl(w):
    w = [i for i in w.lower().replace('qu', 'q') if i.isalpha()]; s = []; z = 0; p = -1
    for i in range(len(w)):
        if w[i] not in 'aeiouy': s.append(0)
        elif w[i] == 'y' and i+1<len(w) and w[i+1] in 'aeiou': s.append(0)
        else: s.append(1)
    if w[-1] == 'e' and not ((len(w)>1 and s[-2]) or (len(w)>2 and w[-2] == 'l' and s[-3] == 0)): z -= 1
    if w[-2:] == ['e', 's'] and not ((len(w)>2 and s[-3]) or (len(w)>3 and s[-3] == s[-4] == 0)): z -= 1
    for i in s:
        if i != p: p = i; z += p
    return max(z, 1)
S = input().split(); H = [[], [], []]; L = [5, 7, 5]; p = 0
for i in S:
    if p == 3: print(' '.join(S)); exit()
    if L[p] >= (s:=syl(i)): H[p].append(i); L[p] -= s
    else: print(' '.join(S)); exit()
    p += L[p] == 0
if p != 3: print(' '.join(S)); exit()
for h in H: print(' '.join(h))