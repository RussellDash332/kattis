F=1;G=H=0
for i in range(2,int(input())):F,G,H=G,H,i*(2*H+(i-1)*F)//2%(10**9+7)
print(H)