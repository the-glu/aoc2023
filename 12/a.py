from utils import *
ensure_data()

data = rdl()

lines = []
values = []

for x in data:
    xx, yy = x.split(" ")
    nl = [xxx for xxx in xx]

    lines.append(nl + ["?"] + nl + ["?"] + nl + ["?"] + nl + ["?"] + nl)

    values.append([int(y) for y in yy.split(",")] * 5)
    # lines.append(nl)
    # values.append([int(y) for y in yy.split(",")])

print(lines, values)


def gen_value_from_line(l):
    vals = []
    isbroken = False
    brokencount = 0
    for x in l:
        if isbroken:
            if x == ".":
                isbroken = False
                vals.append(brokencount)
            else:
                brokencount += 1
        else:
            if x == "#":
                isbroken = True
                brokencount = 1

    if isbroken:
        vals.append(brokencount)
    return vals

# for p, l in enumerate(lines):
#     print(l, values[p], gen_value_from_line(l))

def compute_possible_choices(l, v):
    qpos = []
    for p, x in enumerate(l):
        if x == "?":
            qpos.append(p)
    tt = 0
    for x in range(0, 2**l.count("?")):
        newl = l[::]
        x = "000000000000000000000000000" * 5 + bin(x)[2:]
        for p, y in enumerate(qpos):
            if x[-1-p] == "1":
                newl[y] = "#"
            else:
                newl[y] = "."

        if gen_value_from_line(newl) == v:
            tt += 1

    return tt


ttt = 0

# for p, l in enumerate(lines):
#     print(values[p], l)
#     v = compute_possible_choices(l, values[p])
#     ttt += v
#     print(p, v)
# print(ttt)

import functools
@functools.lru_cache()
def recu_find(l, v, brokenmode):

    # print(l, v, brokenmode)

    if not l:
        if brokenmode is None and not v:
            return 1
        if brokenmode is not None:
            if v == tuple([brokenmode]):
                return 1
        return 0
    tt = 0

    if brokenmode is not None:
        if not v:  # No more broken to find
            return 0

        if brokenmode > v[0]:
            return 0  # echec
        elif brokenmode == v[0]:
            if l[0] == "." or l[0] == "?": # Ok next
                tt += recu_find(l[1:], v[1:], None)
            else:
                return 0 # impssible
        elif brokenmode < v[0]:
            if l[0] == ".":
                return 0  # Echec
            else:
                tt += recu_find(l[1:], v, brokenmode + 1)
    else:
        if (l[0] == "#" or l[0] == "?"):
            tt += recu_find(l[1:], v, 1)  # START BROKEN
        if (l[0] == "." or l[0] == "?"):
            tt += recu_find(l[1:], v, None)

    return tt


for p, l in enumerate(lines):
    print(values[p], l)
    v = recu_find(tuple(l), tuple(values[p]), None)
    ttt += v
    print(p, v)
    # a = 1 / 0
print(ttt)
