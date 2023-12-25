from utils import *
ensure_data()

data = rdl()


m = {}
mx = 0
my = 0
mmx, mmy = 0, 0

px, py = 0, 0

corners = [(0, 0)]
distaround = 0

for i in data:
    i = i.split(" ")
    # if i[0] == "R":
    #     dx, dy = 0, 1
    # elif i[0] == "L":
    #     dx, dy = 0, -1
    # if i[0] == "U":
    #     dx, dy = -1, 0
    # elif i[0] == "D":
    #     dx, dy = 1, 0

    # for d in range(0, int(i[1])):
    #     px += dx
    #     py += dy
    #     m[px, py] = "#"
    #     mx = max(mx, px + 1)
    #     my = max(my, py + 1)
    #     mmx = min(mmx, px)
    #     mmy = min(mmy, py)

    i2 = i[2][2:][:-2]
    dist = int(i2, 16)
    code = i[2][-2]

    if code == "0":
        dx, dy = 0, 1
    elif code == "2":
        dx, dy = 0, -1
    if code == "3":
        dx, dy = -1, 0
    elif code == "1":
        dx, dy = 1, 0

    distaround += dist
    px += dist * dx
    py += dist * dy


    corners.append((px, py))

# for x in range(mmx, mx):
#     for y in range(mmy, my):
#         if (x, y) not in m:
#             m[x, y] = "."
#

# printmap(m, mx, my)
#
# def color(px, py):
#     todo = [(px, py)]
#     while todo:
#         px, py = todo.pop()
#         for nx, ny in around(px, py, croix=False, own=True):
#             if m.get((nx, ny)) == ".":
#                 todo.append((nx, ny))
#                 m[nx, ny] = "#"
#
# color(1, 1)
# # color(1, 207)
#
# print("")
# print("")
# print("")
# printmap(m, mx, my)
#
# tt = 0
# for z in m.values():
#     if z == "#":
#         tt += 1
#
# print(tt)

corners.append((0, 0))
from shapely.geometry import Polygon
pgon = Polygon(corners)

print(pgon.area + distaround / 2 + 1)
