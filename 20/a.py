from utils import *
ensure_data()

data = rdl()

elems = {}

state = {}

connected_states = {}

for x in data:
    a, b = x.split(" -> ")
    if a == "broadcaster":
        a = "bbroadcaster"
    if a == "output":
        a = "ooutput"
    dests = b.split(", ")
    elems[a[1:]] = a[0], dests
    state[a[1:]] = False

    for d in dests:
        if d not in connected_states:
            connected_states[d] = {a[1:]: False}
        else:
            connected_states[d][a[1:]] = False

print(elems)
print(state)
print(connected_states)

actions = []

output = False

nbh = 0
nbl = 0

nb = 0

LAST = {}
DELTAS = {}
CHECK = {}

TARGETS = connected_states["rs"].keys()

def do_step():
    action, value, fr = actions.pop(0)
    global output, nbl, nbh, nb

    if value:
        nbh += 1
    else:
        nbl += 1

    if action == "output":
        # print("!", value)
        output = value
        return

    if action == "rx" and not value:
        print("STOP", nb)

    if action not in elems:
        return

    modtype, params = elems[action]

    if modtype == "b":
        for dest in params:
            actions.append((dest, value, action))
    elif modtype == "%":
        if not value:
            new_state = not state[action]
            for dest in params:
                actions.append((dest, new_state, action))
            state[action] = new_state

    elif modtype == "&":
        connected_states[action][fr] = value

        new_state = not all(connected_states[action].values())
        for dest in params:
            actions.append((dest, new_state, action))
        state[action] = new_state
        if new_state and action in TARGETS:
            if action not in LAST:
                LAST[action] = nb
            else:
                if action not in DELTAS and nb - LAST[action]:
                    print(nb, nb - LAST[action])
                    DELTAS[action] = nb - LAST[action]
                    print(DELTAS)
                    if len(DELTAS.values()) == 4:
                        print(ppcm(*DELTAS.values()))

for x in range(0, 1000000000):
    nb += 1
    actions.append(("broadcaster", False, None))

    while actions:
        do_step()

print(nbl, nbh, nbl * nbh)

    # print(state)
    # print(output)
    # print("")
