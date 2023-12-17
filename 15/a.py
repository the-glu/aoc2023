from utils import *
ensure_data()

data = rdl()

print(len(data))
steps = data[0].split(",")

def ha(s):
    v = 0
    for ss in s:
        v += ord(ss)
        v *= 17
        v = v % 256
    return v

print(ha("HASH"))

tt = 0

for s in steps:
    tt += ha(s)

print(tt)

boxes = {}

for x in range(0, 256):
    boxes[x] = []

for s in steps:
    if s[-1] == "-":
        la = s[:-1]
        bo = ha(la)
        newb = []
        for ol, ov in boxes[bo]:
            if ol != la:
                newb.append((ol, ov))
        boxes[bo] = newb
    else:
        la, v = s.split("=")
        bo = ha(la)
        f = False
        newb = []
        for ol, ov in boxes[bo]:
            if ol == la:
                newb.append((ol, int(v)))
                f = True
            else:
                newb.append((ol, ov))
        if not f:
                newb.append((la, int(v)))
        boxes[bo] = newb

print(boxes)

tt = 0

for x in range(0, 256):

    p = 1
    for ol, ov in boxes[x]:
        print(x + 1, ov, p)
        tt += (x + 1) * ov * p
        p += 1

print(tt)
