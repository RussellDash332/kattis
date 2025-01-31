X=int(input());S=input();P=[]
while S not in P:P.append(S);S=S[::2]+S[1::2][::-1]
print(P[X%len(P)])