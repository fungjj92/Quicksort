from collections import defaultdict, OrderedDict, Counter

fwd = defaultdict(list)
rev = defaultdict(list)
with open("test.txt") as vertices:
    for line in vertices:
        component = line.split()
        fwd[int(component[0])].append(int(component[1]))
with open("test.txt") as vertices:
    for line in vertices:
        component = line.split()
        rev[int(component[1])].append(int(component[0]))

fwd = OrderedDict(fwd)
rev = OrderedDict(rev)

global finish
global visited
global visitedrev
global leaders
global trev
global SCCs
finish = []
visited = []
visitedrev = []
leaders = []
SCCs = Counter()

def DFSLoop(graph):
    for i in reversed(graph):
        if i not in visited:
            leaders.append(i)
            DFS(graph, i)

def DFS(graph, vertex):
    visited.append(vertex)
    stack = graph[vertex]
    while stack:
        w = stack[-1]
        try:
            stack2 = graph[w]
            for edge in stack2:
                if edge not in visited:
                    visited.append(edge)
                    stack.append(edge)
        except:
            finish.append(w)

def DFSOuterRev(rgraph):
    for i in reversed(t):
        if i not in visitedrev:
            leaders.append(i)
            DFSRev(rgraph, i)

print rev
DFSLoop(rev)
print visited