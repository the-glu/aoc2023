from utils import *
ensure_data()

data = rdl()


stones = []

for x in data:
    pp, dd = x.split(" @ ")
    pp = pp.split(", ")
    dd = dd.split(", ")

    stones.append(((int(pp[0]),int(pp[1]),int(pp[2])), (int(dd[0]),int(dd[1]),int(dd[2]))))

from z3 import *

s = Solver()

d = Real('d')
s.add(d > 0)

dx = Real('dx')
dy = Real('dy')
dz = Real('dz')
ix = Real('ix')
iy = Real('iy')
iz = Real('iz')

for sid, stone in enumerate(stones):

    sd = Real(f'{sid}d')

    (s1x, s1y, s1z), (d1x, d1y, d1z) = stone

    s.add(d1x * sd + s1x == ix + dx * sd)
    s.add(d1y * sd + s1y == iy + dy * sd)
    s.add(d1z * sd + s1z == iz + dz * sd)

print(s)


print(s.check())
m = s.model()
print(m)
print(m[ix] + m[iy] + m[iz])
a = 1 / 0


####### P1



def cross_location(s1, s2):
    (s1x, s1y, s1z), (d1x, d1y, d1z) = s1
    (s2x, s2y, s2z), (d2x, d2y, d2z) = s2

    x1 = Real('x1')
    y1 = Real('y1')
    x2 = Real('x2')
    y2 = Real('y2')
    d = Real('d')
    d2 = Real('d2')

    s = Solver()

    s.add(x1 == d1x * d + s1x)
    s.add(y1 == d1y * d + s1y)
    s.add(x2 == d2x * d2 + s2x)
    s.add(y2 == d2y * d2 + s2y)

    mi = 200000000000000
    ma = 400000000000000
    mi = 7
    ma = 27

    s.add(x1 >= mi)
    s.add(x1 <= ma)
    s.add(x2 >= mi)
    s.add(x2 <= ma)
    s.add(y1 >= mi)
    s.add(y1 <= ma)
    s.add(y2 >= mi)
    s.add(y2 <= ma)

    s.add(x1 == x2)
    s.add(y1 == y2)
    s.add(d > 0)
    s.add(d2 > 0)
    # print(s)
    # set_option(rational_to_decimal=True)

    # print(s.check())
    return str(s.check())  == "sat"

    try:
        # print(s.model())
        x = s.model()
        return True
    except:
        return False
    if s.check() == "sat":
        print(s.model())
        return True
    else:
        print("NO")

    # print(solve(x1 == d1x * d + s1x, y1 == d1y * d + s1y, x2 == d2x * d2 + s2x, y2 == d2y * d2 + s2y, x1 == x2, y1 == y2, d > 0, d2 > 0))

from itertools import combinations

tt = 0

v = 0
for a, b in combinations(stones, 2):
    # print(a, b)
    v += 1
    if cross_location(a, b):
        tt += 1
    print(v)

print(tt)





