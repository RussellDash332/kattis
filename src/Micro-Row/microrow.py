# reference: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-34.php
import sys; input = sys.stdin.readline
from bisect import *
p = []
for i in range(n:=int(input())): x, y = map(int, input().split()); p.append((x, (-y, i)))
p = [v for _, v in sorted(p, key=lambda x: x[0])]; c = [None]*n; s = []
class Stack(list):
    def __lt__(s, o): return s[-1][0] < o[-1][0]
for e in p:
    ss = Stack([e]); i = bisect_left(s, ss); c[e[1]] = i+1
    if i != len(s): s[i].append(e)
    else: s.append(ss)
print(*c)