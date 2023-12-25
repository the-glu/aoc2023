from utils import *
ensure_data()

data = rdl()

pomode = False
rules = {}
parts = []

for x in data:
    if not x:
        pomode = True
        continue
    if not pomode:
        rid, rdata = x[:-1].split("{")
        rdata = rdata.split(",")
        rules[rid] = rdata
    else:
        p = {}
        for zz in x[1:-1].split(","):
            k, v = zz.split("=")
            p[k] = int(v)
        parts.append(p)

print(rules, parts)

def apply_rule(rid, part):
    for rule in rules[rid]:
        if ":" in rule:
            cond, result = rule.split(":")

            if ">" in cond:
                k, v = cond.split(">")
                v = int(v)

                if part[k] <= v:
                    continue

            if "<" in cond:
                k, v = cond.split("<")
                v = int(v)

                if part[k] >= v:
                    continue

        else:
            result = rule

        if result == "A":
            return True
        if result == "R":
            return False
        return apply_rule(result, part)

tt = 0
for p in parts:
    result = apply_rule("in", p)
    if result:
        tt += p.get("x", 0)
        tt += p.get("m", 0)
        tt += p.get("a", 0)
        tt += p.get("s", 0)

print(tt)

def ranged_rule_appler(rid, rpos=0):

    rule = rules[rid][rpos]
    print(rid, rpos)

    if rule == "A":
        print("RALL")
        return [[1, 4000, 1, 4000, 1, 4000, 1, 4000]]
    if rule == "R":
        print("RNOTIHNG")
        return []
    if ":" not in rule:
        r = ranged_rule_appler(rule)
        print("Rsimple", r)
        return r

    if ":" in rule:
        cond, result = rule.split(":")

        if result == "A":
            subT = [[1, 4000, 1, 4000, 1, 4000, 1, 4000]]
        elif result == "R":
            subT = []
        else:
            subT = ranged_rule_appler(result)

        subF = ranged_rule_appler(rid, rpos + 1)

        if ">" in cond:
            k, v = cond.split(">")
            v = int(v)

        elif "<" in cond:
            k, v = cond.split("<")
            v = int(v)

        if k == "x":
            i = 0
        if k == "m":
            i = 1
        if k == "a":
            i = 2
        if k == "s":
            i = 3

        def fusion(gt, vv, li):
            new_li = []
            for vals in li:
                new_val = vals[::]
                mi, ma = new_val[i * 2], new_val[i * 2 + 1]

                if gt:
                    mi = max(mi, vv + 1)
                else:
                    ma = min(ma, vv - 1)

                if mi > ma:
                    continue

                new_val[i * 2] = mi
                new_val[i * 2 + 1] = ma

                new_li.append(new_val)

            return new_li

        if ">" in cond:
            ct = fusion(True, v, subT)
            cf = fusion(False, v + 1, subF)
            print(">", rid, rpos, rule, ct, cf)
            return ct + cf
        if "<" in cond:
            ct = fusion(False, v, subT)
            cf = fusion(True, v - 1, subF)
            print("<", rid, rpos, rule, ct, cf)
            return ct + cf


tt = 0
for x in ranged_rule_appler("in"):
    print(x)

    tt += (x[1] - x[0] + 1) * (x[3] - x[2] + 1) * (x[5] - x[4] + 1) * (x[7] - x[6] + 1)


print(tt)
