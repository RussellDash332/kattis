import sys; input = sys.stdin.readline
from array import *
A = array('i'); B = array('i'); n = int(input())
for _ in range(n): x, y = map(int, input().split()); A.append(x); B.append(y)

# this part could've been made O(log n) with bisect but am lazy :)
def f(x): return sum(abs(x-A[i])*B[i] for i in range(n))

a, b = min(A), max(A)
while b-a>2:
    if f(μ:=b-(b-a)//3) >= f(λ:=a+(b-a)//3): b = μ
    else: a = λ
print(min(range(max(1, a-2), b+3), key=f))