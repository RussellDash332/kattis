import sys; input = sys.stdin.readline
from math import *
from collections import Counter
for tc in range(int(input())):
    m = int(input()); c = [*map(int, input().split())]; n, t = map(int, input().split())
    ans = 0; tot = factorial(m)//(factorial(n)*factorial(m-n))
    c1, c2 = c[:m//2], c[m//2:]; h1, h2 = Counter(), Counter()
    for bm in range(1<<len(c1)):
        tt = 0; pc = 0
        for i in range(len(c1)):
            if bm&(1<<i): tt += c1[i]; pc += 1
        h1[(pc, tt)] += 1
    for bm in range(1<<len(c2)):
        tt = 0; pc = 0
        for i in range(len(c2)):
            if bm&(1<<i): tt += c2[i]; pc += 1
        h2[(pc, tt)] += 1
    for pc, tt in h1: ans += h1[(pc, tt)]*h2[(n-pc, t-tt)]
    print('Game', tc+1, '--', ans, ':', tot-ans)