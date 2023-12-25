from utils import *
ensure_data()

data = rdl()

m, mx, my = readmap(data)

sx, sy = 0, 0
for (x, y), p in m.items():
    if p == "S":
        sx, sy = x, y

print(sx, sy)

# possible = [(sx, sy)]

current_pos = [(sx, sy)]

# import functools
#
# hits = 0
# @functools.cache
# def get_pos_for_location(x, y, nb_steps, forbidden):
#     global hits
#     print(x, y, nb_steps, forbidden)
#
#     if nb_steps == 0:
#         # print(x, y, forbidden)
#         hits += 1
#         return 1, [(x, y)]
#
#     tt = 0
#     pos = 0
#     whatidid = []
#
#     for nx, ny in around(x, y, croix=False):
#         if m.get((nx % mx, ny % my)) in [".", "S"]:
#             if (nx, ny) not in forbidden:
#                 subi, sub = get_pos_for_location(nx % mx, ny % my, nb_steps - 1, tuple(whatidid))
#                 tt += subi
#                 whatidid += sub
#             # else:
#             #     print("FOR")
#             # print("  " * (6 - nb_steps), (x, y), subi, substeps)
#             # print("  " * (6 - nb_steps), (x, y), nb_steps, (nx, ny), c)
#
#     return tt, list(set(whatidid))
#
# import sys
# sys.setrecursionlimit(50000)
#
# print(get_pos_for_location(sx, sy, 50, ())[0])
# print(hits)

p = 0
pp = 0

if False:
    for x in range(0, 50000):
        new_pos = set()
        for px, py in current_pos:
            for nx, ny in around(px, py, croix=False):
                if m.get((nx % mx, ny % my)) in [".", "S"]:
                    if (nx, ny) not in new_pos:
                        new_pos.add((nx, ny))
                    # if (nx, ny) not in possible:
                    #     possible.append((nx, ny))

        current_pos = new_pos
        if (x + 1) % 131 == 65:
            print(x, len(current_pos), len(current_pos) - p, len(current_pos) - p - pp)
            pp = len(current_pos) - p
            p = len(current_pos)
        # print(x)

    print(len(current_pos))

#
# 64 3699 3699 3699
# 195 33137 29438 25739
# 326 91951 58814 29376
# 457 180141 88190 29376
# 588 297707 117566 29376
# 719 444649 146942 29376
at64 = 3699
at195delta = 29438
deltaofdelta = 29376


tt = at64
acc = at195delta
for x in range(0, int((26501365 - 65) / 131)):
    tt += acc
    acc += deltaofdelta
print(tt)


