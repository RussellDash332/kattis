from math import *
EPS = 1e-14
LIM = 309
n = int(input())
ori = [[*map(int, input().split('^'))] for _ in range(n)]
pos = [0]*n
fmt = lambda x: print(x, '^'.join(map(str, ori[x])).ljust(40), end=' ')
for i in range(n-1):
    for j in range(i+1, n):
        expi, expj = ori[i].copy(), ori[j].copy()
        if 1 in expi: expi = expi[:expi.index(1)]
        if 1 in expj: expj = expj[:expj.index(1)]
        si = sj = cmpi = cmpj = 1
        infi = infj = 0
        for k in range(len(expi)-1, -1, -1):
            if si*log10(expi[k]) < LIM: si = expi[k] ** si; cmpi = si
            else:
                infi += 1
                if infi == 1: cmpi = si*log(expi[k])
                if infi == 2: cmpi = si*log(expi[k+1]) + log(log(expi[k]))
        for k in range(len(expj)-1, -1, -1):
            if sj*log10(expj[k]) < LIM: sj = expj[k] ** sj; cmpj = sj
            else:
                infj += 1
                if infj == 1: cmpj = sj*log(expj[k])
                if infj == 2: cmpj = sj*log(expj[k+1]) + log(log(expj[k]))
        if infi > infj: pos[i] += 1
        elif infj > infi: pos[j] += 1
        else:
            if (cmpi - cmpj)/(cmpi + cmpj) > EPS: pos[i] += 1
            elif (cmpi - cmpj)/(cmpi + cmpj) < -EPS: pos[j] += 1
            else:
                expi, expj = expi[:infi][:-1], expj[:infj][:-1]
                while expi and expj and expi[-1] == expj[-1]: expi.pop(), expj.pop()
                if not expi and not expj: continue
                if (not expi and expj) or expj[-1] > expi[-1]: pos[j] += 1
                if (expi and not expj) or expi[-1] > expj[-1]: pos[i] += 1
        #fmt(i), print(infi, cmpi), fmt(j), print(infj, cmpj), print('-'*80)
print('Case 1:')
for tow in map(lambda x: '^'.join(map(str, ori[x])), sorted(range(n), key=lambda x: pos[x])): print(tow)