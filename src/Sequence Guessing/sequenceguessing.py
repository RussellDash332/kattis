print(n:=66668); s = set()
while (v:=int(input())) != -1:
    if v == 10**5: print(n)
    elif v%3 == 0: print(2*(v//3)+1)
    elif v%3 == 1:
        if v in s and v+1 in s: assert 0
        elif v in s: print(2*(v//3)+2)
        elif v+1 in s: print(-1)
        else: print(-1); s.add(v+1)
    else:
        if v in s and v-1 in s: assert 0
        elif v in s: print(2*(v//3)+2)
        elif v-1 in s: print(-1)
        else: print(-1); s.add(v-1)
for v in range(10**5+1):
    if v == 10**5 or v%3 == 0: s.add(v)
    elif v%3 == 1:
        if v in s and v+1 in s: assert 0
        elif v in s: pass
        elif v+1 in s: pass
        else: s.add(v+1)
    else:
        if v in s and v-1 in s: assert 0
        elif v in s: pass
        elif v-1 in s: pass
        else: s.add(v-1)
print(*sorted(s))