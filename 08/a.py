from utils import *
ensure_data()

data = rdl()

ins = [x for x in data[0]]

nodes = {}

for ns in data[2:]:
    n, r = ns.split(" = (")
    r, l = r.split(", ")
    nodes[n] = r, l[:-1]

print(nodes)

# pos = "AAA"
# nm = 0
#
# while pos != "ZZZ":
#     for i in ins:
#         pos = nodes[pos][1 if i == "R" else 0]
#         nm += 1
#         if pos == "ZZZ":
#             break
#
# print(nm)

poss = []

for n in nodes.keys():
    if n[-1] == "A":
        poss.append(n)

def do_count(pos):
    nm = 0

    while pos[-1] != "Z":
        for i in ins:
            pos = nodes[pos][1 if i == "R" else 0]
            nm += 1
            if pos[-1] == "Z":
                break
    return nm

c = []

for pos in poss:
    c.append(do_count(pos))

print(ppcm(*c))

# ipos = 0
# nm = 0
# while not all([pos[-1] == "Z" for pos in poss]):
#     i = ins[ipos]
#     ipos += 1
#     if ipos == len(ins):
#         ipos = 0
#
#     npos = []
#
#     for pos in poss:
#         pos = nodes[pos][1 if i == "R" else 0]
#         npos.append(pos)
#
#     poss = npos
#     nm += 1
#     print(i, ipos, nm, poss)
#
# print(nm)
