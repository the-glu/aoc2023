from utils import *
ensure_data()

m = {}

dpos = []

dmode = False
d = ""
at = []

for px,x in enumerate(rdl()):
    dmode = False
    for py, y in enumerate(x):
        m[(px, py)] = y
        if y.isdigit() and not dmode:
            sx, sy = px, py
            dmode = True
            d = y
            at = [(px, py)]
        elif dmode:
            if not y.isdigit():
                dmode = False
                dpos.append((sx, sy, d, at))
            else:
                d += y
                at.append((px, py))
    if dmode:
        dmode = False
        dpos.append((sx, sy, d, at))

print(m)
print(dpos)

s = 0

gear = {}
geared = {}

for dx, dy, d, at in dpos:
    ok = False
    for ax, ay in at:
        for nx, ny in around(ax, ay):
            if m.get((nx, ny), ".") not in ".0123456789":
                ok = True
                if m[(nx, ny)] == "*":
                    if (nx, ny) not in gear:
                        gear[(nx, ny)] = []
                        geared[(nx, ny)] = []

                    if (dx, dy) not in geared[(nx, ny)]:
                        geared[(nx, ny)].append((dx, dy))
                        gear[(nx, ny)].append(int(d))


    # for ax, ay in [at[0]]:
    #     for ddx in [-1, 0, 1]:
    #         for ddy in [-1, 0]:
    #             nx = ax + ddx
    #             ny = ay + ddy
    #             if m.get((nx, ny), ".") not in ".0123456789":
    #                 ok = True
    #
    # for ax, ay in [at[-1]]:
    #     for ddx in [1, 0, -1]:
    #         for ddy in [1, 0]:
    #             nx = ax + ddx
    #             ny = ay + ddy
    #             if m.get((nx, ny), ".") not in ".0123456789":
    #                 ok = True
    if ok:
        s += int(d)

print(s)
print(gear)

tt = 0
for g in gear.values():
    if len(g) == 2:
        tt += g[0] * g[1]

print(tt)

print(list(around(0, 0)))
