N,C=map(int,input().split());A={0};V={*map(int,input().split())}
for _ in'.'*C:
 A={a+v for a in A for v in V if a+v<=C};V={(v+1)//2for v in V}
 if C in A:print('YES');exit()
print('NO')