p=int(input());B=[*map(int,input())]
if p==2:print(B[0]);exit()
L=[];v=0
for i in range(len(B)):L.append(v:=(2*v-p*B[i])%(1<<(i+1))%p)
X=L.pop()
while L:X=(X+p*((2*L.pop()-X)%(1<<(len(L)+1))>0))//2
print(X)