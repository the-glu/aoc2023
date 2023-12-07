from utils import *
ensure_data()

data = rdl()

times = [int(x) for x in data[0].split(":")[1].replace(" ", "").split()]
distances = [int(x) for x in data[1].split(":")[1].replace(" ", "").split()]

print(times, distances)
t = 1
for rid in range(0, len(times)):
    record = 0
    for tentative in range(1, times[rid]):
        vitesse = tentative
        restant = times[rid] - tentative
        distance = vitesse * restant
        if distance > distances[rid]:
            record += 1
        # print(vitesse, restant, distance)
    print(record)
    t *= record

print(t)

