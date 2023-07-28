import sys; input = sys.stdin.readline
def bt(i, v):
    if i < len(p) and v <= R: x.add(v), bt(i, v*p[i]), bt(i+1, v)
while True:
    if not (n:=int(input())): break
    p = [*map(int, input().split())]; x = set()
    L, R = map(int, input().split()); bt(0, 1)
    print('none' if not (s:=sorted(i for i in x if i >= L)) else ','.join(map(str, s)))