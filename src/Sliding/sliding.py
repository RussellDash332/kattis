from collections import*
N=len(S:=input().strip())
M=len(T:=input().strip())
U=Counter(ord(x)-97for x in T)
P=[[0]for _ in'.'*26]
for k in range(N):
 for i in range(26):P[i]+=[P[i][-1]+(S[k]==chr(97+i))]
for i in range(N-M+1):
 if all(P[j][i+M]-P[j][i]==U[j]for j in range(26)):print(i+1)