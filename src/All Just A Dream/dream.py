import sys

def push(event):
    event_map[event] = len(event_stack)
    event_stack.append(event)

def pop():
    if event_stack:
        e = event_stack.pop()
        del event_map[e]
        return e

input()
event_stack = []
event_map = {}
for line in sys.stdin:
    line = line.strip().split()
    if line[0] == 'E':
        push(line[1])
    elif line[0] == 'D':
        for _ in range(int(line[1])):
            pop()
    else: # scenario
        consistent = True
        mn, mx = 0, len(event_stack)
        for event in line[2:]:
            if event[0] != '!':
                if event in event_map:
                    mx = min(mx, len(event_stack) - event_map[event] - 1)
                else:
                    consistent = False
                    break
            else:
                if event[1:] in event_map:
                    mn = max(mn, len(event_stack) - event_map[event[1:]])

        if consistent and mn <= mx:
            if mn == 0:
                print('Yes')
            else:
                print(mn, 'Just A Dream')
        else:
            print('Plot Error')