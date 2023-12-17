from utils import *
ensure_data()

data = rdl()

m = {}
for xp, xx in enumerate(data):
    for xy, d in enumerate(xx):
        m[xp, xy] = d


# dx, dy = 1, 0
#
# beans = [(0, 0)]

touched = []
done = []

def yourou(px, py, dx, dy):

    if (px, py, dx, dy) in done:
        return
    done.append((px, py, dx, dy))

    while (px, py) in m:
        if (px, py) not in touched:
            touched.append((px, py))

        v = m[px, py]


        if v == ".":
            px += dx
            py += dy
        elif v == "-" and dy != 0:
            px += dx
            py += dy
        elif v == "|" and dx != 0:
            px += dx
            py += dy
        elif v == "-" and dy == 0:
            yourou(px, py - 1, 0, -1)
            yourou(px, py + 1, 0, 1)
            return
        elif v == "|" and dx == 0:
            yourou(px - 1, py, -1, 0)
            yourou(px + 1, py, 1, 0)
            return
        elif v == "/":
            if dx == -1:
                dx = 0
                dy = 1
            elif dx == 1:
                dx = 0
                dy = -1
            elif dy == -1:
                dx = 1
                dy = 0
            elif dy == 1:
                dx = -1
                dy = 0
            px += dx
            py += dy
        elif v == "\\":
            if dx == -1:
                dx = 0
                dy = -1
            elif dx == 1:
                dx = 0
                dy = 1
            elif dy == -1:
                dx = -1
                dy = 0
            elif dy == 1:
                dx = 1
                dy = 0
            px += dx
            py += dy


    pass


best = 0

for x in range(0, len(data)):
    touched = []
    done = []

    yourou(x, 0, 0, 1)
    best = max(best, len(touched))
    print(len(touched))

    touched = []
    done = []

    yourou(x, len(data[1]) - 1, 0, -1)
    print(len(touched))
    best = max(best, len(touched))

for y in range(0, len(data[0])):
    touched = []
    done = []

    yourou(0, y, 1, 0)
    best = max(best, len(touched))
    print(len(touched))

    touched = []
    done = []

    yourou(len(data) - 1, y, -1, 0)
    print(len(touched))
    best = max(best, len(touched))


print(best)
