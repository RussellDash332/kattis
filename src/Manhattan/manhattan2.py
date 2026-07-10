X=[];Y=[];W=u=v=0
for _ in'.'*int(input()):x,y,w=map(int,input().split());X+=[(x,w)];Y+=[(y,w)];W+=w
W>>=1
for x,w in sorted(X):
 if u+w>W:break
 u+=w
for y,w in sorted(Y):
 if v+w>W:break
 v+=w
print(x,y)