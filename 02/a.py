from utils import *
ensure_data()

g = {}

for x in rdl("input"):
    y, z = x.split(": ")
    y = y[5:]


    g[y] = []

    for p in z.split("; "):
        mm = {}

        for zz in p.split(", "):
            u, uu = zz.split(" ")
            mm[uu] = int(u)

        g[y].append(mm)

tt = 0
for gi, rd in g.items():
    ok = True
    mr, mg, mb = 0, 0, 0
    for rrd in rd:
        mr = max(mr, rrd.get("red", 0))
        mg = max(mg, rrd.get("green", 0))
        mb = max(mb, rrd.get("blue", 0))
        # if rrd.get("green", 0) > 13:
        #     ok = False
        # if rrd.get("red",0) > 12:
        #     ok = False
        # if rrd.get("blue",0) > 14:
        #     ok = False

    pp = mr * mg * mb

    print(gi, ok, pp)
    # if ok:
    #     tt += int(gi)
    tt += pp

print(tt)

