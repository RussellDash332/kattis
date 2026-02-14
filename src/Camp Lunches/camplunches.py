n,*s,k,x,a,b=map(int,open(0).read().split());d=[1]+[0]*b
for i in s:
 e=[*d]
 for j in range(b-i,-1,-1):e[i+j]|=d[j]
 d=e
for i in range(b,a-1,-1):
 if(i%x<1)*(k*x>=i)*d[i]:print(i);exit()
print('impossible')