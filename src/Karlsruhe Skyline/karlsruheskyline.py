n,a,b=map(int,input().split());L=[*range(n-a+1,n)];R=[*range(n-a,n-a-b+1,-1)]
if 0 in L+R:print('no')
elif L:print('yes',*L,*range(1,n-a-b+2),n,*R)
elif R:print('yes',*L,n,*range(1,n-a-b+2),*R)
else:print('no')