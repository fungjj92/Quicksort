from collections import defaultdict

data = defaultdict(list)
with open("dijkstraData.txt") as f:
    for line in f:
        component = line.split()
        pairs = component[1:]
        for i in pairs:
                v = i.split(",")
                data[int(component[0])].append(v)

def Dijkstra(graph, source):
    processed = [source]
    distTo = defaultdict(list)
    distTo[source] = 0
    V = graph.keys()
    v = source
    V.remove(v)

    while len(V) > 0:
        lenw = float("inf")
        for vertex in processed:
            for edge in graph[vertex]:
                w = int(edge[0])
                if w in V:
                    check = int(edge[1]) + distTo[vertex]
                    if check < lenw:
                        lenw = check
                        newv = w
                    if check < distTo[w]:
                        distTo[w] = check
        v = newv
        processed.append(v)
        V.remove(v)

    return distTo

dists = Dijkstra(data, 1)
print dists[7],dists[37],dists[59],dists[82],dists[99],dists[115],dists[133],dists[165],dists[188],dists[197]


