N=int(input());S={0}
def f(p):
 if p==N:exit()
 input()
 for v in{*map(int,input().split())}-S:S.add(v);print(v);f(v)
 print(p);input();input()
f(0)