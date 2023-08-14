for _ in range(int(input())):
    t, f = input().split()
    v = int(f, 16)
    mantissa = v & ((1<<24)-1)
    if mantissa == 0: print(t, '0'*8); continue
    s = str(v>>31)
    exp = 4*((v>>24)&((1<<7)-1))-257
    while mantissa>>23 != 1: mantissa *= 2; exp -= 1
    if exp > 127: exp = 255; mantissa = 0
    elif exp < -149: exp = mantissa = 0
    elif exp > -127: exp += 127
    else:
        while exp < -126: exp += 1; mantissa //= 2
        exp = 0
    mantissa &= (1<<23)-1
    print(t, hex(int(''.join([s, bin(exp)[2:].zfill(8), bin(mantissa)[2:].zfill(23)]), 2))[2:].upper().zfill(8))