N,K=map(int,input().split());S=input();M=1
while N%2<1<=K:N//=2;K-=1;M*=2
S=M*S[::M];E=1;B=2
if N<2or K<1:print(S),exit(0)
while B-1:E+=1;B=B*2%N
P=pow(2,K%E,N);print(M*''.join(S[P*i%N]for i in range(N)))