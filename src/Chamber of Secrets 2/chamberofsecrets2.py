I=input
for _ in'.'*int(I()):
 n,m=map(int,I().split());B=[[*map(int,I().split())]for _ in'.'*n]
 if n%2==0:print(*sum(sorted(B)[::2],[]))
 else:
  k=min(H:={tuple(b[:m//2]):tuple(b[m//2:])for b in B})
  for _ in'.'*n:print(*k);k=H[k]