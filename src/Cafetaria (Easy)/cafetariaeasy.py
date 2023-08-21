a, b = input().strip().split(), input().strip().split()
bl = ud = bu = ld = None
for _ in range(3):
    for i in range(5):
        if a[2*i] != '_' and b[2*i] != '_': bu = (int(a[2*i]), int(b[2*i]))
        if a[2*i+1] != '_' and b[2*i+1] != '_': ld = (int(a[2*i+1]), int(b[2*i+1]))
        if a[2*i] != '_' and a[2*i+1] != '_': bl = (int(a[2*i]), int(a[2*i+1]))
        if b[2*i] != '_' and b[2*i+1] != '_': ud = (int(b[2*i]), int(b[2*i+1]))
    if bl != None:
        n, d = bl
        for i in range(5):
            if a[2*i] == '_' and a[2*i+1] != '_': a[2*i] = int(a[2*i+1])*n//d
            elif a[2*i+1] == '_' and a[2*i] != '_': a[2*i+1] = int(a[2*i])*d//n
    if ud != None:
        n, d = ud
        for i in range(5):
            if b[2*i] == '_' and b[2*i+1] != '_': b[2*i] = int(b[2*i+1])*n//d
            elif b[2*i+1] == '_' and b[2*i] != '_': b[2*i+1] = int(b[2*i])*d//n
    if bu != None:
        n, d = bu
        for i in range(5):
            if a[2*i] == '_' and b[2*i] != '_': a[2*i] = int(b[2*i])*n//d
            elif b[2*i] == '_' and a[2*i] != '_': b[2*i] = int(a[2*i])*d//n
    if ld != None:
        n, d = ld
        for i in range(5):
            if a[2*i+1] == '_' and b[2*i+1] != '_': a[2*i+1] = int(b[2*i+1])*n//d
            elif b[2*i+1] == '_' and a[2*i+1] != '_': b[2*i+1] = int(a[2*i+1])*d//n
print(*map(int, a)), print(*map(int, b))