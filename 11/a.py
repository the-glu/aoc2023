from utils import *
ensure_data()

data = rdl()

m = {}


for x, d in enumerate(data):
    for y, dd in enumerate(d):
        m[x, y] = dd

toexandx = []
toexandy = []

for y in range(0, len(data[0])):
    toexpand = True
    for x in range(0, len(data)):
        if m[x, y] == "#":
            toexpand = False
    if toexpand:
        toexandy.append(y)

for x in range(0, len(data)):
    toexpand = True
    for y in range(0, len(data[0])):
        if m[x, y] == "#":
            toexpand = False
    if toexpand:
        toexandx.append(x)

print(toexandx, toexandy)

em = {}
dx = 0

for x in range(0, len(data)):
    dy = 0
    for y in range(0, len(data[0])):
        em[x + dx, y + dy] = m[x, y]
        if x in toexandx:
            em[x + dx + 1, y + dy] = m[x, y]
        if y in toexandy:
            dy += 1
            em[x + dx, y + dy] = m[x, y]
            if x in toexandx:
                em[x + dx + 1, y + dy] = m[x, y]

    if x in toexandx:
        dx += 1
    print(x, dx)

print(em)

em = m
dx = 0
dy = 0

for x in range(0, len(data) + dx):
    for y in range(0, len(data[0]) + dy):
        print(em[x, y], end='')
    print("")

gpos = []
for x in range(0, len(data) + dx):
    for y in range(0, len(data[0]) + dy):
        if em[x, y] == "#":
            gpos.append((x, y))

shorted_paths = {}

def find_shorted(sx, sy, dx, dy):
    dist = {}
    todo = [(sx, sy)]
    dist[sx, sy] = 0
    shorted_paths[sx, sy] = {}

    while todo:
        nx, ny = todo.pop(0)
        if (nx, ny) in gpos:
            shorted_paths[sx, sy][nx, ny] = dist[nx, ny]
            # return dist[nx, ny]
        for tx, ty in around(nx, ny, croix=False):
            if (tx, ty) not in dist and (tx, ty) in em:
                bonus = 0
                if tx in toexandx:
                    bonus += 9
                if ty in toexandy:
                    bonus += 9
                dist[tx, ty] = dist[nx, ny] + 1 + bonus
                todo.append((tx, ty))

# print(find_shorted(6, 1, 11, 5))

xx = 0
for x, y in gpos:
    print(xx, len(gpos))
    xx += 1
    find_shorted(x, y, 0, 0)

tt = 0
for v in shorted_paths.values():
    for v2 in v.values():
        tt += v2
print(tt / 2)

# from itertools import combinations
# tt = 0
# c = 0
# l = len(list(combinations(gpos, 2)))
# for c1, c2 in combinations(gpos, 2):
#     tt += find_shorted(c1[0], c1[1], c2[0], c2[1])
#     c += 1
#     print(c, l)
# print(tt)
