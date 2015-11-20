from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from collections import deque
import sys

sys.setrecursionlimit(80000)

data = defaultdict(deque)
rev = defaultdict(deque)

with open("test.txt") as vertices:
    for line in vertices:
        component = line.split()
        data[int(component[0])].append(int(component[1]))
with open("test.txt") as vertices:
    for line in vertices:
        component = line.split()
        rev[int(component[1])].append(int(component[0]))
data = OrderedDict(data)
rev = OrderedDict(rev)

global t
global visited
global visitedrev
global leaders
global trev
global SCCs
t = []
trev = []
visited = []
visitedrev = []
leaders = []
SCCs = Counter()

def DFSOuter(graph):
    for i in reversed(graph):
        if i not in visited:
            DFS(graph, i)

def DFS(graph, vertex):
    visited.append(vertex)
    if vertex not in graph.keys():
        return
    for head in graph[vertex]:
        if head not in visited:
            DFS(graph, head)
    t.append(vertex)
    graph.pop(vertex)

def DFSRev(rgraph, vertex):
    visitedrev.append(vertex)
    if vertex not in rgraph.keys():
        SCCs[leaders[-1]] += 1
        return
    for head in rgraph[vertex]:
        if head not in visitedrev:
            DFSRev(rgraph, head)
    SCCs[leaders[-1]] += 1
    rgraph.pop(vertex, None)

def DFSOuterRev(rgraph):
    for i in reversed(t):
        if i not in visitedrev:
            leaders.append(i)
            DFSRev(rgraph, i)



DFSOuter(data)
#DFSOuterRev(rev)
print visited, t
print Counter(SCCs).most_common(5)


