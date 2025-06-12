N,L,W=map(int,input().split());Z=set()
for _ in'.'*N:x,y=map(int,input().split());Z.add(((x+L-1)//L*L+1,(y+W-1)//W*W+1))
print(len(Z))
for x,y in Z:print(x,y)