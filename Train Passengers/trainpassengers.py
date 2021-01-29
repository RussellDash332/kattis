c,n = list(map(int,input().split(" ")))
inside = 0
result = True
for i in range(n):
    l,e,wait = list(map(int,input().split(" ")))
    if inside < l:
        result = False
    else:
        inside -= l-e
        if ((inside < 0) or (inside > c) or (inside != c and wait > 0) or (i == n-1 and wait != 0)):
            result = False
    
if inside != 0:
    result = False
    
if result:
    print("possible")
else:
    print("impossible")