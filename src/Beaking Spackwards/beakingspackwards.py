N=int(input());A='abcdefghijklmn'
while N:t=int(N**.5);N-=t*t;print(A[:2]*~-t+A[0],end='');A=A[2:]