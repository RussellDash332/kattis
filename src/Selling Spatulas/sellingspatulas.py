import sys; input = sys.stdin.readline
while (n:=int(input())):
    a = [-8]*1440; s = [0]
    for _ in range(n): t, p = map(float, input().split()); a[round(t)] += round(100*p)
    for i in a: s.append(s[-1]+i)
    z = (-1, None, None)
    # lazy to do Kadane :)
    for i in range(1440):
        for j in range(i+1, 1441):
            if s[j] > s[i]: z = max(z, (s[j]-s[i], i-j, -i))
    if z[0] == -1: print('no profit')
    else: print('%.2f'%(z[0]/100), -z[2], -z[2]-z[1]-1)