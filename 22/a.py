from utils import *
ensure_data()

data = rdl()


briks = []

for x in data:
    p1, p2 = x.split("~")
    briks.append(([int(y) for y in p1.split(",")], [int(y) for y in p2.split(",")]))

print(briks)

from functools import cache

@cache
def get_poly_(c1, c2):
    points = []

    if c1 == c2:
        return [c1]

    if c1[0] == c2[0] and c1[1] == c2[1]:
        for x in range(min(c1[2], c2[2]), max(c1[2], c2[2]) + 1):
            points.append([c1[0], c1[1], x])

    if c1[2] == c2[2] and c1[1] == c2[1]:
        for x in range(min(c1[0], c2[0]), max(c1[0], c2[0]) + 1):
            points.append([x, c1[1], c1[2]])

    if c1[0] == c2[0] and c1[2] == c2[2]:
        for x in range(min(c1[1], c2[1]), max(c1[1], c2[1]) + 1):
            points.append([c1[0], x, c1[2]])

    if not points:
        print("HOHO")
        a = 1 / 0

    return points

def get_poly(c1, c2):
    return get_poly_(tuple(c1), tuple(c2))

from collections import defaultdict

def build_supports(mode = -1):
    supported_by = defaultdict(list)

    for bid, (c1, c2) in enumerate(briks):
        underme = []

        points = get_poly(c1, c2)

        for bid2, (b1, b2) in enumerate(briks):
            if bid2 == bid:
                continue

            otherspoints = get_poly(b1, b2)

            supporting = False

            for mypoint in points:
                for otherpoint in otherspoints:
                    if mypoint[0] == otherpoint[0] and mypoint[1] == otherpoint[1] and mypoint[2] == otherpoint[2] + mode:
                        supporting = True
                        break
                if supporting:
                    break
            if supporting:
                supported_by[bid].append(bid2)


    return supported_by

import json
with open("input2") as f:
    briks = json.load(f)

done = True
while not done:
    done = True

    supported_by = build_supports()

    for bid, (c1, c2) in enumerate(briks):
        ok = False
        points = get_poly(c1, c2)
        for mypoint in points:
            if mypoint[2] == 1: # groud
                ok = True

        if ok:
            continue

        for oid, supports in supported_by.items():
            if bid in supports:
                ok = True

        if not ok:
            briks[bid][0][2] -= 1
            briks[bid][1][2] -= 1
            done = False
            print(bid, "Down")
            break

# a = 1 / 0

##########################################
falling = []
for bid, (c1, c2) in enumerate(briks):
    falling.append(bid)

falling = []

while falling:
    working = falling.pop(0)

    c1, c2 = briks[working]

    ok = False
    points = get_poly(c1, c2)
    for mypoint in points:
        if mypoint[2] == 1: # groud, ok for ever
            ok = True

    if ok:
        print(working, "ON THE GOURND")
        continue

    supported_by_done = False
    supported = False

    for bid2, (b1, b2) in enumerate(briks):
        if bid2 == working:
            continue

        if supported_by_done:
            break

        otherspoints = get_poly(b1, b2)

        supporting = False

        for mypoint in points:
            for otherpoint in otherspoints:
                if mypoint[0] == otherpoint[0] and mypoint[1] == otherpoint[1] and mypoint[2] == otherpoint[2] + 1:
                    supporting = True
            if supporting:
                break
        if supporting:
            supported = True
            if bid2 not in falling:
                supported_by_done = True

    if not supported:
        briks[working][0][2] -= 1
        briks[working][1][2] -= 1

    if not supported_by_done:
        falling.append(working)

    print(len(falling))

# import json
# print(json.dumps(briks))


supported_by = build_supports()
supported_by_invert = build_supports(1)
print(supported_by)
print(supported_by_invert)
number_of_suport = defaultdict(lambda: 0)

for oid, supports in supported_by.items():
    for i in supports:
        number_of_suport[i] += 1

non_killable = []

for bid, val in number_of_suport.items():
    if val == 1:

        for oid, supports in supported_by.items():
            if bid in supports:
                print(bid, "is supported by one thing", oid, "is non-killable")
                non_killable.append(oid)

# print(non_killable)
print(len(briks) - len(set(non_killable)))

tt = 0
for bid in set(non_killable):
    moving_set = [bid]
    move = True

    while move:

        move = False

        for oid, support in supported_by_invert.items():
            if oid in moving_set:
                continue

            will_move = True

            for s in support:
                if s not in moving_set:
                    will_move = False
                    break

            if will_move:
                move = True
                moving_set.append(oid)


    tt += len(moving_set) - 1
    print(bid, moving_set)
print(tt)
