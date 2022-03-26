import sys

sys.setrecursionlimit(10001)
v, m = map(int, input().split())
dt = {} # global dependency tree
hm = {}

def build_cost(root):
    if root in hm:
        return hm[root]
    ans = 1
    for k in dt[root]:
        ans += (build_cost(k) * dt[root][k]) % m
    hm[root] = ans % m
    return hm[root]

hm2 = {}
def update_cost(root, widget_set):
    if root in hm2:
        return hm2[root]
    if root in widget_set: # everything below will be included
        return [build_cost(root), 1]
    ans = [0, 0]
    for k in dt[root]:
        cost, update = update_cost(k, widget_set)
        ans[0] += (dt[root][k] * cost) % m
        ans[1] |= update
    # If the children has an update, the root will also be updated
    ans[0] += ans[1]
    ans[0] %= m

    hm2[root] = ans
    return hm2[root]

temp = {}
for line in sys.stdin:
    v -= 1
    temp[len(temp)] = {}
    for k in list(map(int, line.split()))[1:]:
        if k not in temp[len(temp) - 1]:
            temp[len(temp) - 1][k] = 0
        temp[len(temp) - 1][k] += 1
    if v == 0:
        break

q, t = map(int, input().split())

has_cycle = False
status = [0] * len(temp)
def dfs(s):
    global has_cycle
    if has_cycle:
        return
    status[s] = 1
    dt[s] = temp[s]
    for k in temp[s]:
        if status[k] == 1:
            has_cycle = True
        elif status[k] == 0:
            dfs(k)
    status[s] = 2

dfs(0)
if t == 0:
    if 0 not in dt or has_cycle:
        print('Invalid')
    else:
        print(build_cost(0) % m)
        for line in sys.stdin:
            hm2.clear()
            print(update_cost(0, set(map(int, line.split()[1:])))[0] % m)
elif t == 1:
    print(['Invalid', 'Valid'][int(0 in dt and not has_cycle)])