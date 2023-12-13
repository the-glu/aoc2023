from utils import *
ensure_data()

data = rdl()

blocks = []
bdims = []

m = {}

xpos = 0
for x in data:
    if not x:
        blocks.append(m)
        bdims.append((my, xpos))
        m = {}
        xpos = 0
        my = 0
    else:
        for ypos, y in enumerate(x):
            m[xpos, ypos] = y
        my = ypos + 1
        xpos += 1

blocks.append(m)
bdims.append((my, xpos))
print(bdims)

def get_y_line(b, x, wd):
    r = []
    for y in range(0, wd):
        r.append(b[x, y])
    return r

def get_x_line(b, y, hg):
    r = []
    for x in range(0, hg):
        r.append(b[x, y])
    return r

def cmp_lines_delta1(l1, l2):
    one = False
    for pp, ll in enumerate(l1):
        if ll != l2[pp]:
            if one:
                return False, False
            one = True

    return True, one



def find_x_sim(b, wd, hg):

    for posx in range(0, hg):
        isok = True
        hatest = False
        hasonechange = False
        for delta in range(0, hg):
            if posx - delta >= 0 and posx + delta + 1 < hg:
                hatest = True

                print("DIDT EST")
                sameline, changedsomehing =  cmp_lines_delta1(get_y_line(b, posx - delta, wd), get_y_line(b, posx + delta + 1, wd))
                if not sameline or changedsomehing and hasonechange:
                    isok = False
                    break
                if changedsomehing:
                    hasonechange = True
        if isok and hatest and hasonechange:
            print("Rturn", posx)
            return posx + 1

def find_y_sim(b, wd, hg):

    for posy in range(0, wd):
        isok = True
        hatest = False
        hasonechange = False
        for delta in range(0, wd):
            if posy - delta >= 0 and posy + delta + 1 < wd:
                hatest = True
                sameline, changedsomehing =  cmp_lines_delta1(get_x_line(b, posy - delta, hg), get_x_line(b, posy + delta + 1, hg))
                if not sameline or changedsomehing and hasonechange:
                    isok = False
                    break
                if changedsomehing:
                    hasonechange = True
        if isok and hatest and hasonechange:
            return posy + 1

tta = 0
ttb = 0
for p, b in enumerate(blocks):
    y = find_y_sim(b, bdims[p][0], bdims[p][1])
    x = find_x_sim(b, bdims[p][0], bdims[p][1])
    print(p, x, y)
    if y is not None:
        tta += y
    if x is not None:
        ttb += x

print(tta + ttb * 100)

