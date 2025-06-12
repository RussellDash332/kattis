R=[];P=2;C=0
for i in map(int,input()):
 if P!=i:C>0!=R.append((P,C));P=i;C=1
 else:C+=1
R.extend([(P,C),(0,0),(0,0)]);K=len(R)-2;M=[0]*(K+3);U=[0]*(K+1);I=[0]*(K+1);J=[0]*(K+1)
for i in range(K):b,v=R[~i];M[~i-3]=max(M[~i-2],b*v);I[~i-1]=max(I[~i],v+R[~i+1][1]if i>b==0else v);b,v=R[i];U[i+1]=max(U[i],(1-b)*v);J[i+1]=max(J[i],v+R[i-1][1]if i*b else v)
for i in range(K):b,v=R[i];P=max(P,v+sum(R[i+j][1]for j in(-1,1,2)),v+R[i+1][1]+max(M[i+2],U[i]),v+J[i])if b else max(P,v+R[i+1][1],v+I[i+1])
print(P)