from math import*;N,K,*G=map(int,open(0).read().split());D=gcd(*G);M=max(G)
if K>M*M:print('im'*(K%D>0)+'possible')<exit()
D=[1]+[0]*K
for g in G:
 for i in range(K-g+1):D[i+g]|=D[i]
print('im'*(1-D[K])+'possible')