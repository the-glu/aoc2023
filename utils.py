import os
import requests
import sys

def rdl():
    r = []
    fn = "input"
    if "1" in sys.argv:
        fn = "input1"
    if "2" in sys.argv:
        fn = "input2"
    with open(fn) as f:
        for x in f.readlines():
            r.append(x.strip())
    return r

def ensure_data():
    if os.stat("input").st_size == 0:

        directory = os.getcwd()
        directory = directory.split("/")[-1]
        if directory[0] == "0":
            directory = directory[1]
        print(f"Downloading data for {directory}")

        with open("/home/maximilien/.t") as f:
            t = f.read().strip()

        d = requests.get(f"https://adventofcode.com/2023/day/{directory}/input", cookies={"session": t}).text

        if "Please don't repeatedly request this endpoint before it unlocks! The calendar countdown is synchronized with the server time; the link will be enabled on the calendar the instant this puzzle becomes available." in d:
            print("ABORT")
            sys.exit(1)

        with open("input", "w") as f:
            f.write(d)

def around(x, y, croix=True, vertical=True, horizontal=True, own=False):
    deltas = []
    if croix:
        deltas.append((-1, 1))
        deltas.append((-1, -1))
        deltas.append((1, -1))
        deltas.append((1, 1))
    if vertical:
        deltas.append((-1, 0))
        deltas.append((1, 0))
    if horizontal:
        deltas.append((0, 1))
        deltas.append((0, -1))
    if own:
        deltas.append((0, 0))
    for dx, dy in deltas:
        yield (x + dx, y + dy)

## https://python.jpvweb.com/python/mesrecettespython/doku.php?id=pgcd_ppcm
def ppcm(*n):
    def _pgcd(a,b):
        while b:
            a, b = b, a % b
        return a
    p = abs(n[0] * n[1]) // _pgcd(n[0], n[1])
    for x in n[2:]:
        p = abs(p * x) // _pgcd(p, x)
    return p


def readmap(data):
    m = {}
    for xp, xx in enumerate(data):
        for xy, d in enumerate(xx):
            m[xp, xy] = d
    return m, len(data), len(data[0])

def printmap(m, mx, my):
    for x in range(0, mx):
        for y in range(0, my):
            print(m.get((x, y), ''), end='')
        print("")
