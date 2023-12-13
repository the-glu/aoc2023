from utils import *
ensure_data()

data = rdl()

l = []

for x in data:
    l.append([int(y) for y in x.split()])

print(l)

def work(s):
    def build_sub(su):
        dddd = []
        basev = su[0]
        for suu in su[1:]:
            dddd.append(suu - basev)
            basev = suu
        return dddd
    def isz(su):
        for suu in su:
            if suu != 0:
                return False
        return True
    subs = [[y for y in s]]
    cv = s
    while not isz(cv):
        cv = build_sub(cv)
        subs.append(cv)

    cuincrease = 0
    subs[-1].append(0)
    print(subs)

    for su in subs[::-1][1:]:
        su.append(su[0] - cuincrease)
        cuincrease = su[-1]

    print(subs)
    return cuincrease

tt = 0

for x in l:
    tt += work(x)
print(tt)
