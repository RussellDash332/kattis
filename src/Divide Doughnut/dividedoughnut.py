N=int(input())//2;P=5*10**8
def Q(a):print('QUERY',a,(a+P-1)%(2*P));return int(input())
def f(L,R):
 if L==R:print('YES',L)<exit()
 M=(L+R)>>1;K=Q(M)
 if K==N:print('YES',M)<exit()
 elif K<N:f(M+1,R)
 else:f(L,M-1)
f(0,10**9-1)