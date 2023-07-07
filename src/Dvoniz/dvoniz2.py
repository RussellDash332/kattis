import sys
from heapq import *
n, s = map(int, input().split())
a = [*map(int, sys.stdin)]
dp = [[] for _ in range(n)]
# k1[i] = largest k such that sum(a[i-k:i]) <= s
# k2[i] = largest k such that sum(a[i:i+k]) <= s
k1, k2 = [0]*n, [0]*n
ptr1 = ptr2 = curr = 0
while ptr1 < n:
    if ptr2 < n and curr + a[ptr2] <= s: curr += a[ptr2]; ptr2 += 1
    else:
        k2[ptr1] = ptr2-ptr1 # sum(a[ptr1:ptr2]) <= s
        curr -= a[ptr1]; ptr1 += 1
ptr1 = ptr2 = n-2; curr = 0
while ptr1 >= 0:
    if ptr2 >= 0 and curr + a[ptr2] <= s: curr += a[ptr2]; ptr2 -= 1
    else:
        k1[ptr1+1] = ptr1-ptr2 # sum(a[ptr2+1:ptr1+1]) <= s
        curr -= a[ptr1]; ptr1 -= 1
for i in range(n): dp[i-min(k1[i], k2[i])].append(-i)
q = []
for i in range(n):
    for j in dp[i]: heappush(q, j)
    while q and q[0] > -i: heappop(q)
    print(2*(-q[0]-i) if q else 0)