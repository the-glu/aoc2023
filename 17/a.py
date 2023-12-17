from utils import *
ensure_data()

data = rdl()

m, mx, my = readmap(data)


dist = {}

todo = []

PDIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]

# for x, y in m.keys():
#     for d in PDIRS:
#         dist[x, y, d] = 999999999999999999999999
        # todo.append((x, y, d))

for d in PDIRS:
    dist[0, 0, d] = 0
    todo.append((0, 0, 0, d))
visited = []


PRECOMPUTED = {}

for x, y in m.keys():
    for d in PDIRS:
        choices = []

        if d == (0, 1):
            posdir = [(-1, 0), (1, 0)]
        elif d == (0, -1):
            posdir = [(-1, 0), (1, 0)]
        elif d == (1, 0):
            posdir = [(0, -1), (0, 1)]
        elif d == (-1, 0):
            posdir = [(0, -1), (0, 1)]

        choices = []

        for dx, dy in posdir:
            ds = 0
            #for dd in range(1, 4):
            for dd in range(1, 11):
                nx, ny = x + dx * dd, y + dy * dd

                if (nx, ny) in m:
                    ds += int(m[nx, ny])
                    if dd >= 4:
                        choices.append((nx, ny, ds, (dx, dy)))

        PRECOMPUTED[x, y, d] = choices
        # print(choices)

# print(PRECOMPUTED)

from heapq import heappop, heappush

while todo:

    # print(len(todo))

    # todo = sorted(todo, key=lambda t: dist[t[0], t[1], t[2]])
    # mmx, mmy, mdir = todo.pop(0)
    # mv = dist[mmx, mmy, mdir]

    currentbasedist, mmx, mmy, mdir = heappop(todo)

    if (mmx, mmy, mdir) in visited:
        continue
    visited.append((mmx, mmy, mdir))

    # mv = dist[mmx, mmy, mdir]

    if (mmx, mmy) == (mx - 1, my - 1):
        print(currentbasedist)
        break

    choices = PRECOMPUTED[mmx, mmy, mdir]

    for cx, cy, cdelta, ndir in choices:
        # if (cx, cy, ndir) not in visited:
        new_dist = currentbasedist + cdelta

        if new_dist < dist.get((cx, cy, ndir), 999999999999):
            dist[cx, cy, ndir] = new_dist
            heappush(todo, (new_dist, cx, cy, ndir))
