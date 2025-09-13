N=int(input());S=0
for B in range(1,N+1):K=N-~-B//2;T=K//B;S+=B*T*(T+1)//2+(T+1)*(K%B)
print(S/N/N)