import sys
from collections import Counter
n, k = map(int, input().split())
arr = [0]*n
for i, x in Counter(map(int, input().split())).items():
    for j in range(0, n, i): arr[j] += x
cum = [0]; input()
for i in range(n): cum.append(cum[-1] + arr[i])
for l in sys.stdin: L, R = map(int, l.split()); print(cum[R+1]-cum[L])