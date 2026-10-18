N,W=map(int,input().split());K=N//2;T=N-K;f=lambda d:W-d if W+d>1e4else W+d
for k in range(K):print(f(T-~k),k)
for k in range(T):print(f(T-k),K+k)