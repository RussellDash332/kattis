from random import*;R=range
for _ in R(int(input())):
 N=int(input());P=sample(R(4),3)
 for s in P:
  if'T'>input(f'{s//2*"-"}1 {s%2*"-"}2\n'):break
 else:s=6-sum(P)
 Z=[s//2,s%2]+['F'<input(f'{i} {[1,-1][s//2]}\n')for i in R(3,N+1)];print(''.join('FT'[x]for x in Z))