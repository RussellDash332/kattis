from array import *
n, m = map(int, input().split()); a = array('b', map(lambda x: x=='#', input())); s = 0; p = array('i', [s:=s+i for i in a]); ans = 1e18
for i in range(n-m-1):
    if a[i]*a[i+m+1] and ans > p[i+m]-p[i]: ans = p[i+m]-p[i]
print(ans if ans < 1e18 else 'Neibb')