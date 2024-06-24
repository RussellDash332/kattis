from math import gcd
input(); c, d = map(int, input().split()); g = gcd(c, d); c //= g; d //= g; T = 1
while T < c+d: T *= 2
ans = [(1, 2), None, None]

def solve(root, size, needed, left, right):
    stack = [(root, size, needed, left, right)]
    while stack:
        root, size, needed, left, right = stack.pop()
        if needed == 0:         ans[root] = (right, right); continue
        if needed == size:      ans[root] = (left, left); continue
        if needed == size//2:   ans[root] = (left, right); continue
        r = len(ans); ans.append(None) # make new node and assign child
        if needed > size//2:    ans[root] = (left, r); stack.append((r, size//2, needed-size//2, left, right))
        else:                   ans[root] = (r, right); stack.append((r, size//2, needed, left, right))

# it is guaranteed that T-c-d <= T//2 and min(c, d) <= T//2 so we can assign them all to the leaves of a particular subtree
solve(1, T//2, T-c-d, 0, -1 if c > d else -2)
solve(2, T//2, min(c, d), -2 if c > d else -1, -1 if c > d else -2)

print(3*len(ans))
for i, (l, r) in enumerate(ans):
    print(3*i+1, 3*i+2)
    print(3*i, 3*l if l > 0 else l)
    print(3*r if r > 0 else r, 3*i)