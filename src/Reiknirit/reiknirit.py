from collections import*
Z=N=int(input());C=sorted(Counter(input().split()).values())
while C:N-=C.pop();Z+=N
print(Z)