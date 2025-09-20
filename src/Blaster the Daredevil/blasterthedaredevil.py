h=[];m=c=0
for s in[*open(0)][1:]:x,a,b=map(int,s.split());h+=[(a/x,-1),(b/x,1)]
for _,e in sorted(h):m=min(m,c:=c+e)
print(-m)