from utils import *
ensure_data()

data = rdl()

m, mx, my = readmap(data)

import networkx as nx

g = nx.DiGraph()

cpos = (0, 1)
end = (mx - 1, my - 2)


# for (x, y), v in m.items():
    # g.add_node((x, y))

for (x, y), v in m.items():

    if v == "#":
        continue

    ## P1
    # if v == "v":
    #     choices = [(x + 1, y)]
    # elif v == ">":
    #     choices = [(x, y + 1)]
    # else:
    choices = around(x, y, croix=False)

    for nxx, ny in choices:
        dv = m.get((nxx, ny), "#")
        # P1
        # if dv == "." or (dv == "v" and nxx >= x) or (dv == ">" and ny >= y):
        if dv != "#":
            g.add_edge((x, y), (nxx, ny), weight=1)


# Reduce
done = False
while not done:
    done = True

    for n in g.nodes:
        autour = list(g.neighbors(n))

        if len(autour) == 1:  # Deadend
            if n != cpos and n != end:
                g.remove_node(n)
                done = False
                break

        elif len(autour) == 2:  # Fusion
            new_w = g.get_edge_data(autour[0], n)["weight"] + g.get_edge_data(n, autour[1])["weight"]
            g.add_edge(autour[0], autour[1], weight=new_w)
            g.add_edge(autour[1], autour[0], weight=new_w)
            g.remove_node(n)
            done = False
            break

print("Prunned", g)
# l = nx.goldberg_radzik(g, source=cpos, weight= lambda x, z, y: -1)
# print(len(l))

paths = nx.all_simple_edge_paths(g, source=cpos, target=end)
m = 0
tt = 0
for p in paths:
    n = 0
    for pp in p:
        n += g.get_edge_data(*pp)["weight"]
    if n > m:
        m = max(m, n)
        print(m, tt)
    tt += 1
    # d = []
    # for pp in p:
    #     if pp[0] in d:
    #         print("!!!", pp[0])
    #     d.append(pp[0])
    #     print(pp, m.get(pp[0]), m.get(pp[1]))
    #
    # for x in range(0, mx):
    #     for y in range(0, my):
    #         if (x, y) in d:
    #             print("!", end="")
    #         else:
    #             print(m[x, y], end="")
    #     print("")
    #
    # a = 1 / 0
print(m)

# print(end)
#
# dist = {}
# dist[cpos] = 0
# todo = []
# todo.append((0, 0, 1))
#
# from heapq import heappop, heappush
#
# visited = []
#
# while todo:
#     d, cx, cy = heappop(todo)
#     # print(d, cx, cy)
#
#     if (cx, cy) == end:
#         print(dist[cx, cy])
#         break
#
#     visited.append((cx, cy))
#
#     # if m[cx, cy] == "v":
#     #     choices = [(cx + 1, cy)]
#     # elif m[cx, cy] == ">":
#     #     choices = [(cx, cy + 1)]
#     # else:
#     choices = around(cx, cy, croix=False)
#
#     v = dist[cx, cy] + 1
#     for nx, ny in choices:
#         if m.get((nx, ny), "#") != "#" and v >= dist.get((nx, ny), -99999999):
#             if (nx, ny) not in visited:
#                 dist[nx, ny] = v
#                 heappush(todo, (1000000 - v, nx, ny))

# visited = {}
# import sys
# sys.setrecursionlimit(50000)
#
# def recuprom(cx, cy, cv):
#     if (cx, cy) == end:
#         return cv
#
#     visited[(cx, cy)] = True
#     new_v = cv
#
#     for nx, ny in around(cx, cy, croix=False):
#         if m.get((nx, ny), "#") != "#":
#             if not visited.get((nx, ny)):
#                 new_v = max(recuprom(nx, ny, cv + 1), new_v)
#     visited[(cx, cy)] = False
#     return new_v
#
#
# print(recuprom(0, 1, 0))
