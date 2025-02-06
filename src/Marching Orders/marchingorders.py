from math import*;N=int(input());S=[ord(i)-65 for i in input()];A=[*range(N)];T=[[A.index(i),A.remove(i)][0]for i in S]
def bezout(a, b):
 if a==0: return 0,1
 if b==0: return 1,0
 p,q=bezout(b,a%b);return(q,p-a//b*q)
def crt(a,m,b,n):
 d=gcd(m,n)
 if(a-b)%d:print('NO'),exit()
 return(a-m*bezout(m,n)[0]*(a-b)//d)%lcm(m,n)
X=crt(T[0],N,T[1],N-1);L=N*(N-1)
for i in range(2,N-1):X=crt(X,L,T[i],N-i);L=lcm(L,N-i)
print('YES',X)