S='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';R={e:i for i,e in enumerate(S)}
for _ in range(int(input())):
 k,s=input().split();k=int(k);n=len(s);F=[n]*k;T=[0]*-~n;C=[0]*n+[1];x=z=0;y=k;v=set()
 for i in range(n)[::-1]:
  T[i]=x+1;C[i]=y;f=C[F[c:=R[s[i]]]];y,z=((y-f,z),(y,z-f))[c in v];v.add(c);F[c]=i;z+=C[i]
  if len(v)==k:x+=1;v=set();y=z;z=0
  y%=10**9+7
 print(x+1,y)