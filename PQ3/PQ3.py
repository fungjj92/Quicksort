import random
from collections import defaultdict
import math
import copy

data = defaultdict(list)
with open("Mincut.txt") as vertices:
    for line in vertices:
        component = line.split()
        data[int(component[0])] = [int(item) for item in component[1:]]

#global object: pair [] and minCount
global tracker;
tracker = {'pair': [0, 0], 'minCount': 0};

def findMinCount(iterations, dictionary):
    x = 0
    while x < iterations:
        randomContractor(dictionary)
        x += 1
        print x

def randomContractor(dictionary):
    graph = copy.deepcopy(dictionary)
    while len(graph) > 2:
        vertA = random.choice(graph.keys())
        edges = graph[vertA]
        idxB = random.randint(0, len(edges)-1)
        vertB = edges[idxB]
        graph[vertA].pop(idxB)
        for vertex in graph:
            currentEdges = graph[vertex]
            numEdges = len(currentEdges)
            for i in range(0, numEdges):
                if currentEdges[i] == vertB:
                    graph[vertex][i] = vertA
        graph[vertA].extend(graph[vertB])
        del graph[vertB]
        edgeIdx = 0
        while edgeIdx < len(graph[vertA]):
            if graph[vertA][edgeIdx] == vertA:
                graph[vertA].pop(edgeIdx)
            else:
                edgeIdx += 1
    if tracker['minCount'] > len(graph.values()[0]) or tracker['minCount'] == 0:
        tracker['minCount'] = len(graph.values()[0])
        tracker['pair'] = {graph.keys()[0], graph.keys()[1]}


n = int(math.pow(len(data.keys()), 2))
findMinCount(n, data)
print tracker



## SANDBOX ##
#combine lists by non-duplicates# graph[vertA].extend(x for x in graph[vertB] if x not in edgesA)

# PSEUDOCODE -->>
# function input: # times to run this function below
    #while len(graph) > 2
        #var y = random # < len(graph)
        #var yVal
        #var z = random # < len(graph[component]
        #var zVal
        #pop out graph[y[z]]
        #function: search and replace
            #iterate thru graph to find instances of zVal and change to yVal
        #function: merge
            #merge the two vertices of yVal
        #function: delete self loops
            #at graph yVal pop children yVal too
    #new min count comparison
        #if global object count > len(graph[0]):
            #minCount = len(graph[0])
            #pair = [graph.values[0], graph.values()[1]]
