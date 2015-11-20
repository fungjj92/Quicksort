from collections import defaultdict

data = defaultdict(list)
with open("test.txt") as f:
    for line in f:
        component = line.split()
        pairs = component[1:]
        for i in pairs:
                v = i.split(",")
                data[int(component[0])].append(v)

s = 1
processed = [s]
distTo = defaultdict(list)
distTo[s] = 0
V = data.keys()
v = s

while set(processed) != set(V):
    #compare and choose shortest edge in data[v]:
    w = None
    lenw = None
    for edge in data[v]:
        if not lenw or edge[1] < lenw:
            w = int(edge[0])
            lenw = int(edge[1])
    distTo[w] = distTo[v] + lenw
    v = w
    processed.append(v)

print distTo
