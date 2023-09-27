import sys; input = sys.stdin.readline
def lis(arr):
    def upper_bound(sub, idx):
        lo, hi = 0, len(sub) - 1
        while hi > lo:
            mid = (lo + hi) // 2
            if arr[sub[mid]] < arr[idx]: lo = mid + 1
            else: hi = mid
        return hi
    temp = []; par = [None]*len(arr)
    for i in range(len(arr)):
        if not temp or arr[i] > arr[temp[-1]]:
            if temp: par[i] = temp[-1]
            temp.append(i)
        else:
            rep = upper_bound(temp, i); temp[rep] = i
            if rep != 0: par[i] = temp[rep - 1]
    final = 0; curr = temp[-1]
    while curr != None: final += 1; curr = par[curr]
    return final
for tc in range(int(input())):
    n, p, q = map(int, input().split())
    a, b = [*map(int, input().split())], [*map(int, input().split())]
    c = []; r = {e:i for i,e in enumerate(a)}
    for i in range(q+1):
        if b[i] in r: c.append(r[b[i]])
    print(f'Case {tc+1}: {lis(c)}')