from utils import *
ensure_data()

cards = {}
cards_copy = {}

for x in rdl():
    cid, r = x.split(": ")
    cid = int(cid[5:])

    a, b = r.split(" | ")

    wn = [int(v) for v in a.split(" ") if v]
    ln = [int(v) for v in b.split(" ") if v]
    cards[cid] = wn, ln
    cards_copy[cid] = 1

# cards_copy[1] = 1

# s = 0
# for c, (wn, ln) in cards.items():
#     bs = 1
#     for n in ln:
#         if n in wn:
#             bs *= 2
#             print(c, n)
#     print(bs / 2)
#     if bs != 1:
#         s += bs / 2
#
# print(s)

for x in range(1, len(cards_copy.keys()) + 1):
    wn, ln = cards[x]
    m = 0

    for n in ln:
        if n in wn:
            m += 1
    print(x, m)

    if m:
        for y in range(x + 1, x + 1 + m):
            cards_copy[y] += cards_copy[x]
            print("added to ", y, cards_copy[x])

print(cards_copy)

tt = 0
for v in cards_copy.values():
    tt += v
print(tt)
