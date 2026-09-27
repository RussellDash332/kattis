r,c,*a=map(int,open(0).read().split());z,o,t=[*map(a.count,(0,1,2))]
if z>1:print(0)
elif z<1:print(t%2*2**(t//2))
else:print(2-(o>0if~-r*~-c else(1in(a[0],a[-1]))))