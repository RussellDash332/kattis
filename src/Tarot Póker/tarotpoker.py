from itertools import *
hc = ['O', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI']
lc = [a+str(b) for a in 'SBVM' for b in [*range(1, 11)]+[*'GRDK']]
class Card:
    def __init__(self, c):
        self.c = c; self.j = c == 'J'; self.s = 5; self.v = 99
        if self.j: pass
        elif c in hc: self.s = 4; self.v = hc.index(c)
        else: self.s = 'SBVM'.index(c[0]); self.v = int(c[1:]) if c[1] not in 'GRDK' else 'GRDK'.index(c[1])+11
    def __repr__(self): return self.c+str([self.s, self.v])
    def __eq__(self, o): return self.c == o.c
    def __lt__(self, o):
        if self.s == o.s == 4: return self.v < o.v
        if self.s == 4: return 0
        if o.s == 4: return 1
        if self.v == o.v: return self.s < o.s
        return self.v < o.v
ALL = [*map(Card, lc+hc)]
class Deck:
    def __init__(self, cc):
        self.cc = cc
        self.n_joker = sum(c.j for c in cc)
        self.nonjoker = sorted(c for c in cc if not c.j)[::-1]
    def __repr__(self):
        return str(self.cc)
    def rank(self):
        if self.n_joker == 5: return -1, [Card('XXI')]*5
        if self.n_joker == 4: return -1, [Card(self.nonjoker[0].c if self.nonjoker[0].s == 4 else 'M'+self.nonjoker[0].c[1])]*4+self.nonjoker
        candidates = []
        if self.n_joker == 3:
            for i in range(len(ALL)):
                for j in range(i+1):
                    for k in range(j+1): candidates.append(sorted([*self.nonjoker, ALL[i], ALL[j], ALL[k]], reverse=True))
        elif self.n_joker == 2:
            for i in range(len(ALL)):
                for j in range(i+1): candidates.append(sorted([*self.nonjoker, ALL[i], ALL[j]], reverse=True))
        elif self.n_joker == 1:
            for i in range(len(ALL)): candidates.append(sorted([*self.nonjoker, ALL[i]], reverse=True))
        else: candidates.append(self.nonjoker)
        best = (-20, candidates[0])
        for cand in candidates:
            # five of a kind (v = value set)
            if len(v:={c.v*2+(c.s<4) for c in cand}) == 1: best = max(best, (-1, cand)); continue
            if best[0] > -2: continue
            # no lows (d = all diff suits)
            if (d:={c.s for c in cand}) == {4}: best = max(best, (-2, cand)); continue
            if best[0] > -3: continue
            # straight flush (s = is a straight)
            if (s:=all(cand[i+1].v==cand[i].v-1 for i in range(4))) and len(d) == 1: best = max(best, (-3, cand)); continue
            if best[0] > -4: continue
            # diversity
            if len(d) == 5: best = max(best, (-4, cand)); continue
            if best[0] > -5: continue
            # large sum house (m = highest card is a high card, n = other 4 cards are low but comparable)
            if (m:=cand[0].s==4) and (n:=all(cand[i].s < 4 and cand[i].v < 11 for i in range(1, 5))) and cand[0].v == sum(cand[i].v for i in range(1, 5)): best = max(best, (-5, cand)); continue
            if best[0] > -6: continue
            # comparable house
            if m and n and {cand[0].v} == {cand[i].v for i in range(1, 5)}: best = max(best, (-6, cand)); continue
            if best[0] > -7: continue
            # sum house
            if m:
                # second highest card can also be a high card
                if cand[1].s == 4:
                    # the other 3 must be low and comparable
                    if all(cand[i].s < 4 and cand[i].v < 11 for i in range(2, 5)):
                        sc = sum(cand[i].v for i in range(2, 5))
                        if sc == cand[0].v: best = max(best, (-7, [cand[0], *cand[2:], cand[1]])); continue
                        if sc == cand[1].v: best = max(best, (-7, [*cand[1:], cand[0]])); continue
                else:
                    # all 4 cards are low, take one out
                    sc = 0; cm = []; dm = {*range(1, 5)}
                    for i in range(1, 5):
                        if cand[i].s < 4 and cand[i].v < 11: sc += cand[i].v; cm.append(i); dm.remove(i)
                    if len(cm) == 3 and sc == cand[0].v: best = max(best, (-7, [cand[0], *(cand[i] for i in cm), cand[dm.pop()]])); continue
                    if len(cm) == 4:
                        ok = 0
                        while cm:
                            if sc-cand[i:=cm.pop()].v == cand[0].v: best = max(best, (-7, [*cand[:i], *cand[i+1:], cand[i]])); ok = 1; break
                        if ok: continue
            if best[0] > -8: continue
            # numberless
            if all(c.s < 4 and c.v > 10 for c in cand): best = max(best, (-8, cand)); continue
            if best[0] > -9: continue
            # four of a kind
            vv = lambda i: 2*cand[i].v+(cand[i].s<4); ok = 0
            for i in range(5):
                if len({vv(j) for j in range(5) if j != i})==1: best = max(best, (-9, [*cand[:i], *cand[i+1:], cand[i]])); ok = 1; break
            if ok: continue
            if best[0] > -10: continue
            # full house
            if len(v) == 2: best = max(best, (-10, cand)); continue
            if best[0] > -11: continue
            # flush
            if len(d) == 1: best = max(best, (-11, cand)); continue
            if best[0] > -12: continue
            # straight
            if s: best = max(best, (-12, cand)); continue
            # two comparable pairs, comparable pair and pair, comparable pair
            h = {}; u = []
            for i in range(5):
                if vv(i) not in h: h[vv(i)] = []
                h[vv(i)].append(i)
            for bx in [*h]:
                if bx > 21: continue
                if bx in h and bx^1 in h: u.append(h[bx].pop()); u.append(h[bx^1].pop())
                if bx in h and not h[bx]: h.pop(bx)
                if bx^1 in h and not h[bx^1]: h.pop(bx^1)
            u.sort()
            if len(u) == 4: best = max(best, (-13, [cand[i] for i in u]+[cand[i] for i in range(5) if i not in u])); continue
            if len(u) == 2:
                t = max(h, key=lambda x: (len(h[x]), x))
                if len(h[t]) == 2: uu = sorted(u+h.pop(t)); best = max(best, (-14, [cand[i] for i in uu]+[cand[i] for i in range(5) if i not in uu])); continue
                else: best = max(best, (-15, [cand[i] for i in u]+[cand[i] for i in range(5) if i not in u])); continue
            # three of a kind, two pairs, pair
            h = {}
            for i in range(5):
                if vv(i) not in h: h[vv(i)] = []
                h[vv(i)].append(i)
            t = max(h, key=lambda x: (len(h[x]), x))
            if len(h[t]) == 3:
                u = h.pop(t); best = max(best, (-16, [cand[i] for i in u]+[cand[i] for i in range(5) if i not in u])); continue
            elif len(h[t]) == 2:
                u = h.pop(t); tt = max(h, key=lambda x: (len(h[x]), x))
                if len(h[tt]) == 2: uu = sorted(u+h.pop(tt)); best = max(best, (-17, [cand[i] for i in uu]+[cand[i] for i in range(5) if i not in uu])); continue
                else: best = max(best, (-18, [cand[i] for i in u]+[cand[i] for i in range(5) if i not in u])); continue
            # no highs
            if max(d) < 4: best = max(best, (-19, cand)); continue
            # highest card
            best = max(best, (-20, cand))
        return best
K = Deck([*map(Card, input().split())]); k = K.rank()
A = Deck([*map(Card, input().split())]); a = A.rank()
print(-k[0], -a[0]); print(['Jafntefli', 'Konrad', 'Atli'][(k>a)-(k<a)])