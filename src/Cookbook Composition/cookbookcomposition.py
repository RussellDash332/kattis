z={};I=input
for _ in'.'*int(I()):
 r,n=I().split();T={};U={}
 for _ in'.'*int(n):c,t,_,*v=I().split();T[c]=int(t);U[c]=T[c]+max([U[i]for i in v]or[0])
 z[r]=sum(T.values())/max(U.values())
print(*sorted(z,key=z.get))