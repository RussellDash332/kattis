import sys; input = sys.stdin.readline
n = int(input())
m = [input().strip() for _ in range(n)]
o = [0]*n
for i in range(n):
    k = 0; o.sort()
    for j in range(n): k += m[j][i]=='('
    for j in range(n):
        o[j] += 2*(j<k)-1
        if o[j] < 0: print('No'), exit(0)
print('YNeos'[1-(min(o)==max(o)==0)::2])