from utils import *
ensure_data()

tt = 0

ma = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

for x in rdl():
    fd = None
    ld = None

    # print(x)
    # for k, v in ma.items():
    #     x = x.replace(k, str(v))
    # print(x)

    buf = ""
    print(x)

    for y in x:
        if y in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            ld = int(y)
            if fd is None:
                fd = ld

        buf += y
        for k, v in ma.items():
            if buf[(-len(k)):] == k:
                ld = v
                if fd is None:
                    fd = ld


    tt += fd * 10 + ld

print(tt)
