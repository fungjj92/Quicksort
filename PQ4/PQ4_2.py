from collections import defaultdict, OrderedDict, Counter
import sys

sys.setrecursionlimit(80000)

data = defaultdict(list)
rev = defaultdict(list)

with open("SCC.txt") as vertices:
    for line in vertices:
        component = line.split()
        data[int(component[0])].append(int(component[1]))
with open("SCC.txt") as vertices:
    for line in vertices:
        component = line.split()
        rev[int(component[1])].append(int(component[0]))
data = OrderedDict(data)
rev = OrderedDict(rev)

def t1():
    global t
    t += 1
def set(i):
    global s
    s = i
global visited
global visited2
global leaders
global leaders2
global ft
global SCCs
t = 0
s = 0
visited = []
leaders = []
leaders2 = []
ft = []
visited2 = []

def DFSLoop(graph):
    for i in reversed(graph):
        if i not in visited:
            set(i)
            DFS(graph, i)

def DFS(graph, vertex):
    visited.append(vertex)
    leaders.insert(vertex+1, s)
    if vertex in graph.keys():
        for head in graph[vertex]:
            if head not in visited:
                DFS(graph, head)
    t1()
    ft.insert(t, vertex)

def DFSLoop2(graph):
    for i in reversed(ft):
        if i not in visited2:
            set(i)
            DFS2(graph, i)

def DFS2(graph, vertex):
    visited2.append(vertex)
    leaders2.insert(vertex+1, s)
    if vertex in graph.keys():
        for head in graph[vertex]:
            if head not in visited2:
                DFS2(graph, head)

DFSLoop(rev)
DFSLoop2(data)

SCCs = Counter(leaders2)
print SCCs.most_common(5)
