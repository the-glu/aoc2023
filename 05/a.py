from utils import *
ensure_data()

data = rdl()

seeds = [int(y) for y in data[0].split(": ")[1].split()]

maps = {}

mf, nt = None, None

for x in data[2:]:
    if not mf:
        mf, nt = x.split(" map:")[0].split("-to-")
    elif not x:
        mf, nt = None, None
    else:
        if mf not in maps:
            maps[mf] = {}
        if nt not in maps[mf]:
            maps[mf][nt] = []
        dest, source, length = [int(y) for y in x.split()]
        maps[mf][nt].append((source, dest, length))


def apply_maps(numbers, c, dd):
    new_numbers = []
    for n in numbers:
        f = False
        for s, d, l in maps[c][dd]:
            if n >= s and n < s + l:
                new_numbers.append(n + d - s)
                f = True
                break
        if not f:
            new_numbers.append(n)
    return new_numbers


def reverse_map(n, c, dd):
    for s, d, l in maps[c][dd]:
        if n >= d and n < d + l:
            return n - d + s
    return n

# def find_edges(edges, c, dd):
#     new_edges = []
#     for s, d, l in maps[c][dd]:
#         for cfrom, cto in edges:
#             if cfrom >= s and cto >= s + l:
#                 new_edges.append((cfrom, s + l


# def do_block(s):
#     pp = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
#     b = pp[0]
#     v = s
#     for d in pp[1:]:
#         v = apply_maps(v, b, d)
#         b = d
#     return v

pp = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
b = pp[0]
v = seeds


# for d in pp[1:]:
#     v = apply_maps(v, b, d)
#     print(v)
#     b = d
#
# print(v)
# print(min(v))

# new_v = []
# p = 0
# m = 99999999999999999999999999
# while p < len(v):
#     for x in range(v[p], v[p] + v[p + 1]):
#         m = min(m, do_block([x])[0])
#     #     new_v.append(x)
#     p += 2
#     print(p)
# print(m)

stop = False
for x in range(0, 177942185):
    bval = x
    if x % 10000 == 0:
        print(x, int(x / 177942185 * 100) / 100)

    # x = 46

    pp = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    pp = pp[::-1]
    b = pp[0]

    for d in pp[1:]:
        x = reverse_map(x, d, b)
        b = d

    p = 0
    while p < len(seeds):
        if x >= seeds[p] and x < seeds[p] + seeds[p + 1]:
            print(bval)
            stop = True
            break
        p += 2

    if stop:
        break
