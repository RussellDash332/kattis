n, m, l = list(map(int, input().split()))
folds = [l] + list(map(int, input().split()))
cuts = [-l] + list(map(int, input().split())) + [l]
steps = []

for i in range(1, n + 1):
    steps.append(folds[i - 1] - folds[i])
steps.append(l - sum(steps))

events = [(c, 0) for c in cuts]
start = 0
for i in range(n + 1):
    step = steps[i]
    if i % 2: # to the left
        end = start - step
        events.extend([(start, -1), (end, 1)])
    else: # to the right
        end = start + step
        events.extend([(start, 1), (end, -1)])
    start = end
events.sort()
events.pop(0)
lens = []
dd, lvl, prev = 0, 0, events[0][0]
for pt, dl in events:
    dd += (pt-prev)*lvl
    lvl += dl
    prev = pt
    if dl == 0:
        lens.append(dd)
        dd = 0
print(*lens)