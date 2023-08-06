# Similar to https://i.stack.imgur.com/w8qkh.png
V = 0
for p in range(int(input())):
    for t in range(int(input())):
        f, *xyz = map(float, input().split()); v = []
        for i in range(round(f)): v.append((xyz[3*i], xyz[3*i+1], xyz[3*i+2]))
        if t == 0: p = v[0]
        q = v[0]
        for i in range(len(v)-1): s = v[i]; c = v[i+1]; V += abs(sum((q[j]-p[j])*((s[(j+1)%3]-q[(j+1)%3])*(c[(j+2)%3]-q[(j+2)%3])-(s[(j+2)%3]-q[(j+2)%3])*(c[(j+1)%3]-q[(j+1)%3])) for j in range(3)))
print('%.2f'%(V/6))