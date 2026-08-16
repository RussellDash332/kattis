H,W=[dict(zip('IJLOSTZ',k))for k in([1,2,2,0,1,1,1],[1,3,3,2,2,2,2])];T=[]
while(s:=input())!='W':
 print(H[s],end=' ')
 if sum(T)+W[s]<=10:print(sum(T)+1);T+=[W[s]]
 elif W[s]in T:print(sum(T[:T.index(W[s])])+1)
 else:print(1)