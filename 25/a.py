from utils import *
ensure_data()

data = rdl()

m = {}

import networkx as nx
g = nx.Graph()

for x in data:
    s, dests = x.split(": ")
    dests = dests.split(" ")

    if s not in m:
        m[s] = []

    for d in dests:
        if d not in m:
            m[d] = []
        m[d].append(s)
        m[s].append(d)
        g.add_edge(s, d)

l = []

tocut = nx.minimum_edge_cut(g)
print(tocut)

for f, t in tocut:
    g.remove_edge(f, t)

grps = list(nx.connected_components(g))
print(grps, len(grps[0]) * len(grps[1]))
