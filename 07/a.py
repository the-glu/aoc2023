from utils import *
ensure_data()

data = rdl()

from collections import Counter
vorder = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

def order(cards):
    c = Counter(cards)
    # print(c, len(c))
    if len(c) == 1:
        return 1
    if len(c) == 2:
        if c.most_common()[0][1] == 4:
            return 2
        else:
            return 3
    elif len(c) == 3:
        if c.most_common()[0][1] == 3:
            return 4
        else:
            return 5
    elif len(c) == 4:
            return 6
    return 7

def is_better(c1, c2):
    for x, v in enumerate(c1):
        v2 = c2[x]
        vv = vorder.index(v)
        vv2 = vorder.index(v2)
        if vv < vv2:
            return True
        elif vv > vv2:
            return False
    return None

hands = []

def border(h):
    best = 99
    bnh = [x for x in h]
    for nv1 in vorder[:-1] if bnh[0] == "J" else ["X"]:
        for nv2 in vorder[:-1] if bnh[1] == "J" else ["X"]:
            for nv3 in vorder[:-1] if bnh[2] == "J" else ["X"]:
                for nv4 in vorder[:-1] if bnh[3] == "J" else ["X"]:
                    for nv5 in vorder[:-1] if bnh[4] == "J" else ["X"]:
                        nh = [x for x in h]
                        if nh[0] == "J":
                            nh[0] = nv1
                        if nh[1] == "J":
                            nh[1] = nv2
                        if nh[2] == "J":
                            nh[2] = nv3
                        if nh[3] == "J":
                            nh[3] = nv4
                        if nh[4] == "J":
                            nh[4] = nv5
                        nh = "".join(nh)
                        best = min(best, order(nh))

    return best

for p, x in enumerate(data):
    h, s = x.split(" ")
    o = border(h)
    hands.append((h, o, int(s)))
    print(p)
print(hands)

def ordered(i1, i2):
    if i1[1] < i2[1]:
        return -1
    if i1[1] > i2[1]:
        return 1
    v = is_better(i1[0], i2[0])
    if v is None:
        return 0
    if v:
        return -1
    return 1

import functools
hands = sorted(hands, key=functools.cmp_to_key(ordered))
hands = hands[::-1]

s = 0
for p, hand in enumerate(hands):
    s += (p + 1) * hand[2]
print(s)
