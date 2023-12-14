from utils import *
ensure_data()

data = rdl()

m = {}

opos = []

for xp, xx in enumerate(data):
    for xy, d in enumerate(xx):
        m[xp, xy] = d
        if d == "O":
            opos.append((xp, xy))

print(opos, m)

def m_to_n(rx, ry, dx, dy):
    done = False
    while not done:
        if m.get((rx + dx, ry + dy), "") == ".":
            m[rx, ry] = "."
            m[rx + dx, ry + dy] = "O"
            rx += dx
            ry += dy
        else:
            return rx, ry

for x in range(0, 20):
    for y in range(0, 20):
        print(m.get((x, y), ''), end='')
    print("")


# nopos = []
# for px, py in opos:
#     nopos.append(m_to_n(px, py, -1, 0))

def d():
    for x in range(0, 11):
        for y in range(0, 11):
            print(m.get((x, y), ''), end='')
        print("")

for xx in range(0, 1000000000):
    # if x % 1000 == 0:
    #     print(x, x / 1000000000 * 100)

    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:

        nopos = []
        change = True
        while change:
            for px, py in opos:
                nopos.append(m_to_n(px, py, dx, dy))
            if nopos != opos:
                opos = nopos
                nopos = []
                change = True
            else:
                change = False
        # d()


    tt = 0
    for (x, y), v in m.items():
        if v == "O":
            tt += len(data) - x

    print(xx, tt)


for x in range(0, 20):
    for y in range(0, 20):
        print(m.get((x, y), ''), end='')
    print("")

tt = 0
for (x, y), v in m.items():
    if v == "O":
        tt += len(data) - x

print(tt)
