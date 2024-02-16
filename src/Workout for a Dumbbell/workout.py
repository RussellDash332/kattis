ur = [*map(int, input().split())]
u = ur[::2]; r = ur[1::2]; t = 0
uu, rr, tt = map(list, zip(*([*map(int, input().split())] for _ in range(10)))); ss = tt.copy()
# tt[i]: when's the next available time for machine i
for _ in range(3):
    for i in range(10):
        start = t >= ss[i]
        if start: # update machine's next available time
            tt[i] = t-(t-max(tt[i], ss[i]))%(uu[i]+rr[i])
            nn = tt[i]+uu[i]+rr[i] # incorporate recovery time of person i
            tt[i] = max(tt[i]+uu[i], t) # see if person i can do one more rep
        if not start or t > tt[i]: t += u[i]; tt[i] = t
        else: t = tt[i] + u[i]; tt[i] = t
        t += r[i]
        if start: tt[i] = max(tt[i], nn)
print(t-r[-1])