from utils import *
ensure_data()

data = rdl()

m = {}
spos = 0, 0

for x, d in enumerate(data):
    for y, dd in enumerate(d):
        if dd in [".", "S"]:
            m[(x, y)] = (dd, [])
        if dd == "S":
            spos = x, y
            # inputdep
            import sys
            if len(sys.argv) == 1:
                m[(x, y)] = (dd, [(x - 1, y), (x + 1, y)])
            else:
                m[(x, y)] = (dd, [(x + 1, y), (x, y - 1)])
        if dd == "|":
            m[(x, y)] = (dd, [(x - 1, y), (x + 1, y)])
        if dd == "-":
            m[(x, y)] = (dd, [(x, y - 1), (x, y + 1)])
        if dd == "L":
            m[(x, y)] = (dd, [(x - 1, y), (x, y + 1)])
        if dd == "J":
            m[(x, y)] = (dd, [(x - 1, y), (x, y - 1)])
        if dd == "7":
            m[(x, y)] = (dd, [(x + 1, y), (x, y - 1)])
        if dd == "F":
            m[(x, y)] = (dd, [(x + 1, y), (x, y + 1)])

# def find_c_to(x, y):
#     r = []
#     for (nx, ny), (v, item) in m.items():
#         for ix, iy in item:
#             if ix == x and iy == y:
#                 r.append((nx, ny))
#     return r


reverse_mapping = {}
for (nx, ny), (v, item) in m.items():
    for ix, iy in item:
        if (ix, iy) not in reverse_mapping:
            reverse_mapping[ix, iy] = []
        reverse_mapping[ix, iy].append((nx, ny))

def find_c_to(x, y):
    return reverse_mapping.get((x, y), [])


dists = {}
dists[spos] = 0
todo = [spos]

while todo:
    tx, ty = todo.pop()
    for cx, cy in find_c_to(tx, ty):
        if (cx, cy) not in m[tx, ty][1]:
            continue
        if (cx, cy) not in dists:
            dists[cx, cy] = dists[tx, ty] + 1
            todo.append((cx, cy))
        else:
            oldd = dists[cx, cy]
            dists[cx, cy] = min(dists[cx, cy], dists[tx, ty] + 1)
            if oldd != dists[cx, cy] and (cx, cy) not in todo:
                todo.append((cx, cy))

print(dists)

for x in range(0, len(data)):
    for y in range(0, len(data[0])):
        print(m.get((x, y), [''])[0], end="")
    print("")

for x in range(0, len(data)):
    for y in range(0, len(data[0])):
        print(dists.get((x, y), ' '), end="")
    print("")

mm = 0
for d in dists.values():
    mm = max(d, mm)

print(mm)


newm = {}

for (x, y), d in m.items():
    if (x, y) in dists and (not d[1] or (d[1][0] in dists and d[1][1] in dists)):
        newm[(x, y)] = d


def epurage(m2):
    newmm = {}

    for (x, y), d in m2.items():
        if not d[1]:
            newmm[(x, y)] = d
        else:
            if d[1][0] in m2 and d[1][1] in m2:
                if (x, y) in m[d[1][0]][1] or not m[d[1][0]][1]:
                    if (x, y) in m[d[1][1]][1] or not m[d[1][1]][1]:
                        newmm[(x, y)] = d

    return newmm


for x in range(0, 300):
    newm = epurage(newm)

for x in range(0, len(data)):
    for y in range(0, len(data[0])):
        print(newm.get((x, y), ['@'])[0], end="")
    print("")


expended_map = {}

for (x, y), d in newm.items():
    if d[0] != ".":
        rx = x * 2 + 1
        ry = y * 2 + 1
        expended_map[(rx, ry)] = "X"
        for dx, dy in d[1]:
            expended_map[(rx - x + dx, ry - y + dy)] = "X"



for x in range(0, len(data) * 2):
    for y in range(0, len(data[0]) * 2):
        print(expended_map.get((x, y), [' '])[0], end="")
    print("")

spos = 0, 0
todo = [spos]

while todo:
    tx, ty = todo.pop()
    expended_map[(tx, ty)] = "O"
    for x, y in around(tx, ty, croix=False):
        if x < 0 or y < 0:
            continue
        if x > len(data) * 2 or y > len(data[0]) * 2:
                continue
        if (x, y) not in expended_map:
            expended_map[(x, y)] = "O"
            todo.append((x, y))

for x in range(0, len(data) * 2):
    for y in range(0, len(data[0]) * 2):
        print(expended_map.get((x, y), [' '])[0], end="")
    print("")


tt = 0
for x in range(0, len(data)):
    for y in range(0, len(data[0])):
        if newm.get((x, y), ['@'])[0] in ['@', '.']:
            rx = x * 2 + 1
            ry = y * 2 + 1

            if expended_map.get((rx, ry), ' ') != "O":
                tt += 1
                print("I", end='')
            else:
                print(" ", end='')
        else:
            print("-", end='')
    print("")


print(tt)
