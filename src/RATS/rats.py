for _ in range(int(input())):
    k, m, rats = map(int, input().split())
    vis, ok = {rats}, 1
    creep = str(rats)
    if creep.startswith('1233') and creep.endswith('334444') and {*creep[2:-4]} == {'3'}: print(k, 'C', 1); ok = 0
    elif creep.startswith('5566') and creep.endswith('667777') and {*creep[2:-4]} == {'6'}: print(k, 'C', 1); ok = 0
    else:
        for i in range(m-1):
            rats = int(''.join(sorted(str(int(''.join(str(rats)[::-1])) + rats))))
            if rats not in vis: vis.add(rats)
            else: print(k, 'R', i+2); ok = 0; break
            creep = str(rats)
            if creep.startswith('1233') and creep.endswith('334444') and {*creep[2:-4]} == {'3'}: print(k, 'C', i+2); ok = 0; break
            if creep.startswith('5566') and creep.endswith('667777') and {*creep[2:-4]} == {'6'}: print(k, 'C', i+2); ok = 0; break
    if ok: print(k, rats)