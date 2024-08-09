m = n = int(input()); s = input(); r = int(input()); z = w = 0
for i in s:
    if i == 'C':
        if w*z: m = min(m, z)
        z = w = 0
    else: z += 1; w |= i == 'W'
print('IM'*(m<2*r+1)+'POSSIBLE')